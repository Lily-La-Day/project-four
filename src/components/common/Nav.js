import React from 'react'
import Auth from '../../lib/Auth'

import { Link, withRouter } from 'react-router-dom'

class Nav extends React.Component {
  constructor() {
    super()

    this.state = { }



  }




  render() {

    return(
      <nav className="navbar">



        {!Auth.isAuthenticated() && <Link to="/register" className="nav-item nav-one">Register</Link>}
        {!Auth.isAuthenticated() && <Link to="/writerlogin" className="nav-item nav-two">Log In to Write</Link>}
        {!Auth.isAuthenticated() && <Link to="/editorlogin" className="nav-item nav-three">Log In to Edit</Link>}
        {Auth.isAuthenticated() && <Link to="/writerprofile" className="nav-item nav-four">My Writings</Link>}
        {Auth.isAuthenticated() && <Link to="/" className="nav-item nav-four" onClick={() => Auth.logout()}>Log Out</Link>}
        {Auth.isAuthenticated() && <Link to="/submit" className="nav-item nav-four"></Link>}
        <Link to="/writings" className="nav-item nav-three">The Writings</Link>



      </nav>
    )
  }
}

export default withRouter(Nav)
