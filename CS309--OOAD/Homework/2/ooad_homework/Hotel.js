function initial() {

}

function view_declaration_form() {
    let declaration_form = document.getElementById("hotel_declare_form");
    if (declaration_form.style.display === "block") {
        declaration_form.style.display = "none";
    } else {
        declaration_form.style.display = "block";
    }
}

function onClickAddHotel() {
    let hotel_name = document.forms[0][name="hotel_name"].value;
    let city = document.forms[0][name="city"].value;
    let district = document.getElementById("district").value;
    let room_type = document.getElementById("room_type").value;
    let date = document.forms[0][name="date"].value;
    let price = document.forms[0][name="price"].value;

    if (validateInput(hotel_name, city, district, room_type, date, price)) {
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
    let district = document.getElementById("district").value;
    let date = document.forms[0][name="date"].value;
    let earliest_check_in_time = document.forms[0][name="time"].value;
    let price = document.forms[0][name="price"].value;
    let room_type = document.getElementById("room_type").value;
    let rowCount = bodyObj.rows.length;
    let cellCount = bodyObj.rows[0].cells.length;
    bodyObj.style.display = "";
    let newRow = bodyObj.insertRow(rowCount++);
    newRow.insertCell(0).innerHTML = hotel_name;
    newRow.insertCell(1).innerHTML = city;
    newRow.insertCell(2).innerHTML = district;
    newRow.insertCell(3).innerHTML = date;
    newRow.insertCell(4).innerHTML = earliest_check_in_time;
    newRow.insertCell(5).innerHTML = price;
    newRow.insertCell(6).innerHTML = room_type;
    newRow.insertCell(7).innerHTML = bodyObj.rows[0].cells[cellCount - 1].innerHTML;
    bodyObj.rows[0].style.display = "none";
}

function validateInput(hotel_name, city, district, room_type, date, price) {
    let hotel_name_regex = new RegExp(/^[A-Za-z\s]+$/);
    let price_regex = new RegExp(/^\d*$/)
    if(!hotel_name_regex.test(hotel_name)) {
        alert("Input hotel name contains invalid characters !\n(Hotel name can only contains English letters and space)");
        return false;
    }
    if(!price_regex.test(price)) {
        alert("Input price contains invalid characters !\n(Price can only contains numbers)");
        return false;
    }

    //date check
    let cur_date = new Date();
    let tar_date = new Date(date.substring(0, 4), date.substring(5, 7) - 1, date.substring(8, 10));
    if (tar_date < cur_date) {
        alert("Input date must after today !")
        return false;
    }

    //uniqueness check
    let cur_table = document.getElementById("hotel list");
    for (let i = 2, rows = cur_table.rows.length; i < rows; i++) {
        if (cur_table.rows[i].cells[0].innerHTML === hotel_name &&
            cur_table.rows[i].cells[1].innerHTML === city &&
            cur_table.rows[i].cells[2].innerHTML === district &&
            cur_table.rows[i].cells[6].innerHTML === room_type) {
            alert("Different rows with the same Hotel Name, City, District and Room Type can not be appeared for many times.");
            return false;
        }
        if (cur_table.rows[i].cells[0].innerHTML === hotel_name &&
            cur_table.rows[i].cells[1].innerHTML === city &&
            cur_table.rows[i].cells[2].innerHTML === district &&
            cur_table.rows[i].cells[5].innerHTML === price) {
            alert("Price should not be same if different rows have the same Hotel Name, City and District, but the Room Type is difference.");
            return false;
        }
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