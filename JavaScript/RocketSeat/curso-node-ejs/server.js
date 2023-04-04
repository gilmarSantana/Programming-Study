const express = require('express')
const app = express()

app.set("view engine", "ejs")

app.get("/", function(req, res){
    const items = [
        {title: "D", message: "esenvolver aplicações/serviços de forma fácil"},
        {title: "E", message: "JS usa JavaScript para renderizar HTML"},
        {title: "M", message: "uito fácil de usar"},
        {title: "A", message: "morzinho"},
        {title: "I", message: "nigualável"},
        {title: "S", message: "intaxe simples"}
    ]

    const subtitle = "Uma linguagem de modelagem para criação de página HTML usando JavaScript"

    res.render("pages/index", {
        qualitys: items,
        subtitle: subtitle
    })
})

app.get("/about", function(req, res){
    res.render("pages/about")
})

app.listen(8081)
console.log("Runnig on port 8081")