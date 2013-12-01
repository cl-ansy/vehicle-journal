function changeVehicle(targetId, contentId, vehicleId){
    $('#' + targetId).load("/?vid=" + vehicleId + " #" + contentId);
}
