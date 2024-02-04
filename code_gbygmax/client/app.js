  function onClickedpredict() {
    console.log("Estimate button clicked");
    var strain = document.getElementById("strain").value;
    var density = document.getElementById("density").value;
    var pressure = document.getElementById("pressure").value;
    var location = document.getElementById("locations").value;
    

    var result = document.getElementById("result");
  
    var url = "http://127.0.0.1:5000/prediction"; 
  
    $.post(url, {
        strain: strain,
        location: location,
        RD: density,
        conf_pressure: pressure
    },function(data, status) {
        result.innerHTML = data.prediction.toString() ;

    });
    
  }
  


function onPageLoad() {

  var url = "http://127.0.0.1:5000/get_location_names";

  $.get(url,function(data, status) {
      if(data) {
          var locations = data.locations;

          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#locations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;