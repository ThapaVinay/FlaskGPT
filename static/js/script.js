
async function postData(url="", data={})
{
    const response = await fetch(url,{
        method:"POST",
        headers:{
            "Content-Type" : "application/json",
        },
        body: JSON.stringify(data),
    });
    return response.json();
}


sendButton.addEventListener("click", async ()=>{
    question = document.getElementById("question").value;
    document.getElementById("question").value = "";
    document.querySelector(".right2").style.display = "flex";
    document.querySelector(".right1").style.display = "none";

    ques.innerHTML = question;

    // Get the answer and populate
    let result = await postData("/api", {"question" : question});
    const formatResult = result.result.replace(/\n/g, '<br>');
    ans.innerHTML = formatResult;
    // ans.innerHTML = result.result;

})




