import React from 'react'
import { Link } from 'react-router-dom'




class Home extends React.Component {
  constructor() {
    super()

  }



  render() {

    return(
      <Link to="/register" >
        <main className="home">

        </main>
      </Link>
    )
  }
}

export default Home
