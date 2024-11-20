function calculator(ev)
{
  document.getElementById("girilecekrakamid").style.color = "#010101";
  document.getElementById("sonucid").style.color = "#8A8A8A";
  girilenrakamlar = document.getElementById("girilecekrakamid").textContent;
  if(event.currentTarget.innerText!="=")
  {
    document.getElementById("girilecekrakamid").innerHTML = girilenrakamlar+event.currentTarget.innerText;
  }
  
  if(event.currentTarget.innerText=="C")
  {
    document.getElementById("girilecekrakamid").innerHTML = "";
    document.getElementById("sonucid").innerHTML = "";
  }
  
  else if(event.currentTarget.innerText=="<-|")
  {
    document.getElementById("girilecekrakamid").innerHTML = girilenrakamlar.slice(0,-1);
    document.getElementById("sonucid").innerHTML = "";
  }
  
  else if(event.currentTarget.innerText=="=")
  {
    try{
      document.getElementById("sonucid").innerHTML = eval(girilenrakamlar.replace(/×/g,"*").replace(/÷/g,"/"))
    }
    catch(err) {
       document.getElementById("sonucid").innerHTML = "ERROR";
       document.getElementById("girilecekrakamid").style.color = "#C2185B";
       document.getElementById("sonucid").style.color = "#C2185B";
       
    }
  }
}

