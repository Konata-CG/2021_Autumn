function initial() {
    // let year = document.getElementById("year");
    // year.innerHTML = "";
    // year.options.add(new Option("--", null));
    // for (let i = 2000; i <= 2020; i++) {
    //     year.options.add(new Option(i, i));
    // }
}

function onClickAddHotel() {
    let hotel_name = document.forms[0][name="hotel_name"].value;
    let date = document.forms[0][name="date"].value;
    let time = document.forms[0][name="time"].value;
    let room_type = document.getElementById("room_type").value;
    let price = document.forms[0][name="price"].value;
    let hour = time.substring(0,2);
    let min = time.substring(3,5);
    alert(hour + " " + min);
    if (validateInput(hotel_name, date, price)) {
        addRow();
    }
}

function addRow() {
    let bodyObj = document.getElementById("tbody");
    if (!bodyObj) {
        alert("Body of Table not Exist!");
        return;
    }
    let hotel_name = document.forms[0][name="hotel_name"].value;
    let city = document.forms[0][name="city"].value;


    let year = document.getElementById("year").value;
    let month = document.getElementById("month").value;
    let day = document.getElementById("day").value;
    let dhour = document.getElementById("dhour").value;
    let dminute = document.getElementById("dminute").value;
    let ahour = document.getElementById("ahour").value;
    let aminute = document.getElementById("aminute").value;
    let rowCount = bodyObj.rows.length;
    let cellCount = bodyObj.rows[0].cells.length;
    bodyObj.style.display = ""; // display the tbody
    let newRow = bodyObj.insertRow(rowCount++);
    newRow.insertCell(0).innerHTML = document.forms[0]["flight-no"].value;
    newRow.insertCell(1).innerHTML = document.forms[0]["airline-company"].value;
    newRow.insertCell(2).innerHTML = document.forms[0].from.value;
    newRow.insertCell(3).innerHTML = document.forms[0].to.value;
    newRow.insertCell(4).innerHTML = year + "/" + month + "/" + day;
    newRow.insertCell(5).innerHTML = dhour + ":" + dminute;
    newRow.insertCell(6).innerHTML = ahour + ":" + aminute;
    newRow.insertCell(7).innerHTML = bodyObj.rows[0].cells[cellCount -
    1].innerHTML; // copy the "delete" button
    bodyObj.rows[0].style.display = "none"; // hide first row
}

function validateInput(hotel_name, date, price) {
    let hotel_name_regex = new RegExp(/^[A-Za-z\s]+$/);
    if(!hotel_name_regex.test(hotel_name)) {
        alert("Input hotel name contains invalid characters !\n(Hotel name can only contains English letters and space)");
        return false;
    }
    let cur_date = new Date();
    let tar_date = new Date(date.substring(0, 4), date.substring(5, 7) - 1, date.substring(8, 10));
    if (tar_date < cur_date) {
        alert("Input date must after today !")
        return false;
    }
    let price_regex = new RegExp(/^\d*$/)
    if(!price_regex.test(price)) {
        alert("Input price contains invalid characters !\n(Price can only contains numbers)");
        return false;
    }
    return true;
}

function removeRow(inputObj) {
    if (!inputObj) return;
    let parentTD = inputObj.parentNode;
    let parentTR = parentTD.parentNode;
    let parentTBODY = parentTR.parentNode;
    parentTBODY.removeChild(parentTR);
}

function setDistrict() {
    let city = document.forms[0]["city"].value;
    let district = document.getElementById("district");
    if (city === "SHEN ZHEN") {
        district.innerHTML = "";
        district.options.add(new Option("FU TIAN", "FU TIAN"));
        district.options.add(new Option("LUO HU", "LUO HU"));
        district.options.add(new Option("LONG GANG", "LONG GANG"));
        district.options.add(new Option("PING SHAN", "PING SHAN"));
        district.options.add(new Option("LONG HUA", "LONG HUA"));
        district.options.add(new Option("GUANG MING", "GUANG MING"));
        district.options.add(new Option("YAN TIAN", "YAN TIAN"));
    } else if (city === "GUANG ZHOU") {
        district.innerHTML = "";
        district.options.add(new Option("YUE XIU", "YUE XIU"));
        district.options.add(new Option("LI WAN", "LI WAN"));
        district.options.add(new Option("HAI ZHU", "HAI ZHU"));
        district.options.add(new Option("TIAN HE", "TIAN HE"));
        district.options.add(new Option("BAI YUN", "BAI YUN"));
        district.options.add(new Option("HUANG PU", "HUANG PU"));
        district.options.add(new Option("FAN YU", "FAN YU"));
        district.options.add(new Option("HUA_DU", "HUA_DU"));
        district.options.add(new Option("NAN_SHA", "NAN_SHA"));
        district.options.add(new Option("ZENG_CHENG", "ZENG_CHENG"));
        district.options.add(new Option("CONG_HUA", "CONG_HUA"));
    } else {
        alert("invalid city selection !")
    }
}