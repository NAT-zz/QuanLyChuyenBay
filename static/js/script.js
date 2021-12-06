function deleteVe(ve) {
    if (confirm("Bạn có chắc chắn trả vé này không?") == true) {
        fetch("/api/tra-ve/"+ve, {
            method: "delete"
        }).then(function(res) {
            return res.json()
        }).then(function(data) {
            if (data.error_code == 200) {
                alert("Trả vé thành công!")
                location.reload()
            } else{
                alert("Đã xảy ra lỗi! Vui lòng kiểm tra lại thông tin và thử lại!")
        }})
    }
}

function doiVe(ve, id_chuyenBay, hangVe) {
        fetch("/api/doi-ve/"+ve, {
            method: "put",
            body: JSON.stringify({
                "id_chuyen_bay": id_chuyenBay,
                "hang_ve": hangVe
            }),
            headers: {
                "Content-Type": "application/json"
            }
        }).then(function(res) {
            return res.json()
        }).then(function(data) {
            if (data.error_code == 200) {
                alert("Đổi vé thành công!")
            } 
            else{
                if (data.error_code == 404)
                    alert("Đã xảy ra lỗi! Vui lòng kiểm tra lại thông tin và thử lại!")
                else
                    alert("Đã hết vé cho chuyến bay này! Vui lòng chọn chuyến bay khác")          
            }
        })
}


function checkVe(ve, action, id_chuyenBay, hangVe) {
    fetch("/api/check-ve/"+ve, {
        method: "post"
    }).then(function(res) {
        return res.json()
    }).then(function(data) {
        if (data.error_code == 404)
            alert("Vé đã quá thời gian trả không tồn tại hoặc đã quá thời gian đổi trả!")
        else
        {
            if (action==0)
            {
               doiVe(ve, id_chuyenBay, hangVe)
            } 
            else
                deleteVe(ve)
        }
    })
}
