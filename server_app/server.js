const express=require('express')
const app=express()
const http=require('http').createServer(app);
const socket=require('socket.io')(http,{cors:{origin:"*"}})
app.get('/',(req,res)=>{
    res.send("Hey there")
})
http.listen(6767);