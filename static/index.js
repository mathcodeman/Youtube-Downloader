function GetSelectedValue(){
    var e = document.getElementById("audios");
    var selectedValue = e.options[e.selectedIndex].value; 
    document.getElementById("result").innerHTML = selectedValue;
}

function formSubmit(a){
    a.getElementsByTagName("form")[0].submit();
}