import React from 'react'
import Auth from '../../lib/Auth'

import { Link, withRouter } from 'react-router-dom'

class Nav extends React.Component {
  constructor() {
    super()

    this.state = { type: ''  }





  }

  pathCheck() {
    console.log(this.props.location.pathname)
    if(this.props.location.pathname.includes('edit'))
      this.setState({ type: 'editor' })
    else this.setState({ type: 'writer' })
  }

  componentDidMount() {
    this.pathCheck()
  }





  render() {
    console.log(this.props)
    console.log(this.state)
    return(
      <nav className="navbar">


        {!Auth.isAuthenticated() && <Link to='/writingsubmit' className="nav-item nav-one">Submit a Writing</Link>}
        {!Auth.isAuthenticated() && <Link to="/register" className="nav-item nav-one">Register</Link>}
        {!Auth.isAuthenticated() && <Link to="/writerlogin" className="nav-item nav-two" onClick={()=>this.props.pathCheck()}>Log In to Write</Link>}
        {!Auth.isAuthenticated() && <Link to="/editorlogin" className="nav-item nav-three" onClick={()=>this.props.pathCheck()}>Log In to Edit</Link>}
        {Auth.isAuthenticated() && (this.props.type === 'writer'  || this.state.type === 'writer') && <Link to="/writerprofile" className="nav-item nav-four">My Writings</Link>}
        {Auth.isAuthenticated() && <Link to="/" className="nav-item nav-four" onClick={() => Auth.logout()}>Log Out</Link>}
        {(this.props.type === 'writer' || this.state.type === 'writer' ) && Auth.isAuthenticated() && <Link to="/submit" className="nav-item nav-four">Submit Writing</Link>}
        {(this.props.type === 'editor' || this.state.type === 'editor') && Auth.isAuthenticated() && <Link to="/edit-writings" className="nav-item nav-three">The Writings</Link>}



      </nav>
    )
  }
}

export default withRouter(Nav)
