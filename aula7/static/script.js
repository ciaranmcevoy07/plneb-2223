function deleteTerm(designation){
    $.ajax("/term/" + designation, {
        type:"DELETE"
    })

}