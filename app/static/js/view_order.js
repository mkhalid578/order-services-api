
$(document).ready(function(){

    var orderupdateVar;  // updating order table using interval
    var CURRENT_USER_EMAIL = "xyz@gmail.com" //defauly set to ingonre ajax error


    document.getElementById("View-Order").onclick = function() {view_order()};
    document.getElementById("Place-Order").onclick = function() {place_order()};
    document.getElementById("Delete-Order").onclick = function() {delete_order()};



    /* =================== GET CURRENT USER EMAIL FUNCTIONALITY =================== */
        
        function UpdateCurrentUserEmail() {
                // Update data about logged user data from database
                $.ajax({
                          type : "GET",
                          url : "/dashboard/user-email",
                          success: function(result) {
                             CURRENT_USER_EMAIL = result
                             placed_order_table.ajax.url("/api/v1/orders/" + String(CURRENT_USER_EMAIL));
                             placed_order_editing_table.ajax.url("/api/v1/orders/" + String(CURRENT_USER_EMAIL));
                             $("#place-order-email").val(CURRENT_USER_EMAIL)     // logged in user email
                             document.getElementById("Place-Order").disabled = false;
                             console.log(CURRENT_USER_EMAIL);
                          },
                          error: function(error) {
                              console.log(error);
                          }
                });
        }

        UpdateCurrentUserEmail();



    /* =================== PLACE ORDER FUNCTIONALITY =================== */

    function place_order(){
      document.getElementById("view-order-data").style.display ="none";
      document.getElementById("delete-order-data").style.display ="none";
      // clear form
      $("#place-order-item-name").val("");
      $("#place-order-quantity").val("");
      $("#place-order-cost").val("");
      $("#place-order-reason").val("");
      document.getElementById("place-order-error").style.display ="none";
      clearTimeout(orderupdateVar);
    }

    document.getElementById("Placing-Order-btn").onclick = function() {saving_place_order()};

    function saving_place_order(){

                    if ((($("#place-order-email").val()).trim() == "") ||
                        (($("#place-order-item-name").val()).trim() == "") ||
                        (($("#place-order-quantity").val()).trim() == "") ||
                        (($("#place-order-cost").val()).trim() == "") ||
                        (($("#place-order-reason").val()).trim() == "")){
                           document.getElementById("place-order-error").style.display ="block";
                    } else {
                        var obj_data = {
                                      "order-email-id" : $("#place-order-email").val(),
                                      "order-item-name" : $("#place-order-item-name").val(),
                                      "order-item-quentities" : $("#place-order-quantity").val(),
                                      "order-item-cost" : $("#place-order-cost").val(),
                                      "order-reason" : $("#place-order-reason").val()
                                   }
                        var new_order_data = JSON.stringify(obj_data);
                        console.log(new_order_data);
                        $.ajax({
                            type : "GET",
                            url : "/dashboard/place-order",
                            data : { key : new_order_data},
                            dataType : 'json',
                            contentType : 'application/json; charset=utf-8',
                            success : function(data) {
                               console.log(data);
                            }
                        });

                       // clear form
                          $("#place-order-item-name").val("");
                          $("#place-order-quantity").val("");
                          $("#place-order-cost").val("");
                          $("#place-order-reason").val("");
                        // Closing dialog input box
                        document.getElementById("place-order-error").style.display ="none";
                        $('#placeOrder').modal('hide')

                    }


    }



    /* =================== VIEW ORDER FUNCTIONALITY =================== */

    function view_order(){
      document.getElementById("view-order-data").style.display ="block";
      document.getElementById("delete-order-data").style.display ="none";
      $("#placed-order-table").DataTable().draw();
      orderupdateVar = setInterval( UpdateOrderDataPriodically, 30000 );
      placed_order_table.ajax.reload( null, false ); // user paging is not reset on reload;
    }

    function UpdateOrderDataPriodically() {
                // Update order data from database at every mint
                // setInterval( UpdateOrderDataPriodically, 60000 );
                placed_order_table.rows().remove();
                placed_order_table.ajax.reload( null, false ); // user paging is not reset on reload;
    }

    var placed_order_table =
            $("#placed-order-table").DataTable(
                  { "ajax": {
                               "url":  "/api/v1/orders",
                               "dataSrc": function (result) {
                                              var obj = [];
                                              for ( var i=0; i < (result.orders).length ; i++ ) {
                                                    obj.push((result.orders)[i]);
                                              }
                                              upload_order_data_table(obj);
                                          }
                            },
                    "columns" : [ {"title" : "ItemNumber"},
                         {"title" : "Email-Id"},
                         {"title" : "Item-Name"},
                         {"title" : "Item-Quentities"},
                         {"title" : "Item-Cost", 
                          "render" : $.fn.dataTable.render.number( ',', '.', 0, '$' ) },
                         {"title" : "Description"}],

                    "info" : false,
                    "ordering": true,
                    "scrollX" : "500px",
                    "scrollCollapse" : false,
                    "searching" : false});

            document.getElementsByClassName("dataTables_scroll")[0].style.overflow = "scroll";
            document.getElementsByClassName("dataTables_scrollHead")[0].style.overflow = "";
            document.getElementsByClassName("dataTables_scrollBody")[0].style.overflow = "";

    function upload_order_data_table(obj){
                 for(var i = 0; i < obj.length; i++){
                    placed_order_table.row.add([
                                  obj[i]["id"],
                                  obj[i]["email"],
                                  obj[i]["itemName"],
                                  obj[i]["quantity"],
                                  obj[i]["cost"],
                                  obj[i]["description"]
                             ])
                 }
                 placed_order_table.draw(false); // redraw
    }


    /* =================== DELETE ORDER FUNCTIONALITY =================== */
    // NOTE: vibhuti needs to do
    // just show order which are not ordered (placed out order)
    // Also just order of that log in - email_id account


    function delete_order(){
      document.getElementById("view-order-data").style.display ="none";
      document.getElementById("delete-order-data").style.display ="block";
      $("#placed-order-editing-table").DataTable().draw();
      placed_order_editing_table.ajax.reload( null, false ); // user paging is not reset on reload;
      clearTimeout(orderupdateVar);
    }


    var placed_order_editing_table =
            $("#placed-order-editing-table").DataTable(
                  { "ajax": {
                               "url":  "/api/v1/orders",
                               "dataSrc": function (result) {
                                              var obj = [];
                                              for ( var i=0; i < (result.orders).length ; i++ ) {
                                                    obj.push((result.orders)[i]);
                                              }
                                              upload_order_data_editing_table(obj);
                                          }
                            },
                    "columns" : [ {"title" : "ItemNumber"},
                         {"title" : "Email-Id"},
                         {"title" : "Item-Name"},
                         {"title" : "Item-Quentities"},
                         {"title" : "Item-Cost", 
                          "render" : $.fn.dataTable.render.number( ',', '.', 0, '$' ) },
                         {"title" : "Description"},
                         {"data": null,
                          "className": "center",
                          "defaultContent": '<a href="" class="editor_remove">Delete</a>'}
                         ],

                    "info" : false,
                    "ordering": true,
                    "scrollX" : "500px",
                    "scrollCollapse" : false,
                    "searching" : false});

            document.getElementsByClassName("dataTables_scroll")[1].style.overflow = "scroll";
            document.getElementsByClassName("dataTables_scrollHead")[1].style.overflow = "";
            document.getElementsByClassName("dataTables_scrollBody")[1].style.overflow = "";

 
    // Delete a record
    $('#placed-order-editing-table').on( 'click', 'a.editor_remove', function (e) {
        e.preventDefault();
        console.log("remove");
        if (selected_order_detail != ""){ 
           display_deleting_order_data(selected_order_detail);
        }
    });
 
    // Selected raw data from deleting process by users
    var selected_order_detail = "";
    $('#placed-order-editing-table tbody').on( 'click', 'tr', function () {
                  placed_order_editing_table.$('tr.selected').removeClass('selected');
                  $(this).addClass('selected');
                  selected_order_detail = placed_order_editing_table.row('.selected').data();

                  //NOTE: display selected data and open dialog box for confirmation about
                  //      deleting process
                  console.log(selected_order_detail);
    });

    function display_deleting_order_data(obj){
             console.log(obj);
             $("#delete-order-email-data").val(obj[1])     // (obj.id)
             $("#delete-order-itemName-data").val(obj[2])  // (obj.itemName)
             $("#delete-order-quantity-data").val(obj[3])  // (obj.quantity)
             $("#delete-order-cost-data").val(obj[4])      // (obj.cost)
             $("#delete-order-reason-data").val(obj[5])    // (obj.description)
 
             $('#DeleteOrder').modal('show')
    }

    function upload_order_data_editing_table(obj){
                 for(var i = 0; i < obj.length; i++){
                    placed_order_editing_table.row.add([
                                  obj[i]["id"],
                                  obj[i]["email"],
                                  obj[i]["itemName"],
                                  obj[i]["quantity"],
                                  obj[i]["cost"],
                                  obj[i]["description"]
                             ])
                 }
                 placed_order_editing_table.draw(false); // redraw
    }


    document.getElementById("delete-order-submit").onclick = function() {deleting_place_order()};

    function deleting_place_order(){
        if (selected_order_detail != ""){ 
           deleting_order_data_id = parseInt(selected_order_detail[0]);
        }
        $.ajax({
               type : "POST",
               url : "/api/v1/order/edit/" + deleting_order_data_id,
               success : function(data) {
                   console.log(data);
               }
        });
        $('#DeleteOrder').modal('hide')
        //NOTE: display selected data and open dialog box for confirmation about
        //      deleting process
        //      call Ajax, and run delete proce
        selected_order_detail = "";
        placed_order_editing_table.ajax.reload( null, false ); // user paging is not reset on reload;
    }



});

