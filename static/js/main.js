document.getElementById("downloadBtn").addEventListener("click", function(){
    const fbUrl = document.getElementById("fbUrl").value.trim();
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "⏳ Đang tải...";

    if(!fbUrl){
        resultDiv.innerHTML = `<span class="error">❌ Vui lòng nhập link video Facebook!</span>`;
        return;
    }

    fetch("/download", {
        method: "POST",
        body: new URLSearchParams({fb_url: fbUrl}),
        headers: {"Content-Type": "application/x-www-form-urlencoded"}
    })
    .then(res => res.json())
    .then(data => {
        if(data.success){
            resultDiv.innerHTML = `<span class="success">${data.message}</span>`;
        } else {
            resultDiv.innerHTML = `<span class="error">${data.message}</span>`;
        }
    })
    .catch(err => {
        console.log(err);
        resultDiv.innerHTML = `<span class="error">❌ Lỗi kết nối server</span>`;
    });
});
