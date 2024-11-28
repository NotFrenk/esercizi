import './NavBar.css'
import Link from './Link'
const x = 11;
const img = "vite.svg"
const img2 = "vite"

const imgStyle = {
   height: x < 10? "800px" : "100px",
   borderRadius: "30px"
}


function NavBar() {
   return(
      <>
      <div id="boxe" className='rotola'> CIAOOOO</div>
      <nav>{x.toFixed}</nav>
      <nav>{x > 1000? "sono in alto!!" : "sono in basso!!"}</nav>
      <img style={imgStyle} src={img}></img>
      <img className='bordoarrotondato' src={img2 + ".svg"}></img>
      <img className='bordoarrotondato' src={`/${img2}.svg`}></img>

      <ul>
         <li><Link></Link></li>
         <li><Link></Link></li>
         <li><Link></Link></li>
         <li><Link></Link></li>
         <li><Link></Link></li>
      </ul>
      </>
   )
}
export default NavBar