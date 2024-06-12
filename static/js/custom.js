$(document).ready(function () {
  $(".increment-btn").click(function (e) {
    e.preventDefault();

    // var inc_value = $(this).closest(".product_data").find(".qty-input").val();
    // var inc_value = $(".qty-input").val();
    var $el = $(this).closest(".product_data")
    var inc_value = $el.find(".qty-input").val()


    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 10) {
      value++;
      // $(this).closest(".product_data").find(".qty-input").val(value);
      $el.find(".qty-input").val(value);

    }
  });

  $(".decrement-btn").click(function (e) {
    e.preventDefault();

    // var dec_value = $(this).closest(".product_data").find(".qty-input").val();
    var $el = $(this).closest(".product_data")
     var dec_value = $el.find(".qty-input").val();

    var value = parseInt(dec_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 1) {
      value--;
      // $(this).closest(".product_data").find(".qty-input").val(value);
       $el.find(".qty-input").val(value);

    }
  });

  $(".addToCartBtn").click(function (e) {
    e.preventDefault();

    // var product_id = $(this).closest("product_data").find(".prod_id").val();
    var $el = $(this).closest(".product_data")
    var product_id = $el.find(".prod_id").val();
    var product_qty = $el.find(".qty-input").val();
    // var product_qty = $(this).closest("product_data").find(".qty-input").val();

    // console.log(product_qty);
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/add-to-cart",
      data: {
        'product_id': product_id,
        'product_qty': product_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        console.log(response);
        alertify.success(response.status);
      },
    });
  });


  $(".addToWishlist").click(function (e) {
    e.preventDefault();

    // var product_id = $(this).closest("product_data").find(".prod_id").val();
    var $el = $(this).closest(".product_data")
    var product_id = $el.find(".prod_id").val();

    // console.log(product_qty);
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/add-to-wishlist",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        console.log(response);
        alertify.success(response.status);
      },
    });
  });



  $(".changeQuantity").click(function (e) {
    e.preventDefault();

    // var product_id = $(this).closest("product_data").find(".prod_id").val();
    // var product_qty = $(this).closest("product_data").find(".qty-input").val();
    var $el = $(this).closest(".product_data")

    // var product_id = $(".prod_id").val();
    var product_id = $el.find(".prod_id").val();
    var product_qty = $el.find(".qty-input").val();
    // var product_qty = $(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/update-cart",
      data: {
        'product_id': product_id,
        'product_qty': product_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        // console.log(response);
        alertify.success(response.status);
      },
    });
  });



  $(".delete-cart-item").click(function (e) {
    e.preventDefault();

    // var product_id = $(".prod_id").val();
    var $el = $(this).closest(".product_data")
    var product_id = $el.find(".prod_id").val();
    
    console.log(product_id);
    var token = $("input[name=csrfmiddlewaretoken]").val();
    
    $.ajax({
      method: "POST",
      url: "/delete-cart-item",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        $(".cartdata").load(location.href + ".cartdata");
      },
    });
  });
  
  
  $(document).on('click','.delete-wishlist-item', function(e) {
  // $(".delete-wishlist-item").click(function (e) {
    e.preventDefault();

    var $el = $(this).closest(".product_data")
    var product_id = $el.find(".prod_id").val();
    
    // var product_id = $(".prod_id").val();
    console.log(product_id);
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/delete-wishlist-item",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        $(".wishlistdata").load(location.href + ".wishlistdata");
      },
    });
  });

});
