import {useState} from "react";

export default function App(){

const[q,setQ]=useState("")
const[a,setA]=useState("")
const[c,setC]=useState([])

const ask=async()=>{

const r=await fetch(`http://127.0.0.1:8000/ask?q=${q}`)
const j=await r.json()

setA(j.answer)
setC(j.context)

}

return(

<div style={{padding:40}}>

<h2>RAG Assistant</h2>

<input
style={{width:400}}
value={q}
onChange={e=>setQ(e.target.value)}
/>

<button onClick={ask}>Ask</button>

<h3>Answer</h3>
<p>{a}</p>

<h3>Retrieved Context</h3>

{c.map((x,i)=><p key={i}>{x}</p>)}

</div>

)
}