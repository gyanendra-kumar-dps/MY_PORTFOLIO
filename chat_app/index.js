import { initializeApp } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-app.js"
import { getFirestore, doc, setDoc,updateDoc,arrayUnion,onSnapshot} from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js"
import {getAuth,GoogleAuthProvider,signInWithPopup,signOut,onAuthStateChanged} from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
const firebaseConfig = {
apiKey: "AIzaSyDkOsCFgJ34QwEu88xErpDABGm4Fg1zTbY",
authDomain: "simplechatapp-b486a.firebaseapp.com",
projectId: "simplechatapp-b486a",
storageBucket: "simplechatapp-b486a.firebasestorage.app",
messagingSenderId: "704746762460",
appId: "1:704746762460:web:6aa3acad5ab62047720419",
measurementId: "G-BBDV5HMGTL"
}
const app = initializeApp(firebaseConfig)
const db = getFirestore(app);
const collectiondb=doc(db,"main","chat")
const myid=crypto.randomUUID()
const auth=getAuth()
const provider=new GoogleAuthProvider();
async function sendMessage(){
    const new_message=document.getElementById("user-input").value
    const message_got={message:new_message,id:myid,time:new Date()}
    await updateDoc(collectiondb,{Message:arrayUnion(message_got)})
    let user_box=document.createElement('div')
    user_box.className="message sent"
    user_box.textContent=new_message
    let container=document.getElementById("chat-box")
    container.appendChild(user_box)
    container.scrollTop=container.scrollHeight
}
async function login(){
    const res=await signInWithPopup(auth,provider);
    console.log(res)
}
document.getElementById("send-btn").addEventListener("click",sendMessage)
document.getElementById("send-btn").addEventListener("click",login)
onSnapshot(collectiondb,(x)=>{
    const data_recieved=x.data().Message
    const updated_data=data_recieved[data_recieved.length-1]
    if(!(myid==updated_data.id)){
        let user_box=document.createElement('div')
        user_box.className="message received"
        user_box.textContent=updated_data.message
        let container=document.getElementById("chat-box")
        container.appendChild(user_box)
        container.scrollTop=container.scrollHeight
    }
})    