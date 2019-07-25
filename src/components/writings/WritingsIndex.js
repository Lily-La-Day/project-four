import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'



class WritingsIndex extends React.Component {
  constructor() {
    super()

    this.state = { writings: null }


  }

  componentDidMount() {
    axios.get('/api/writings')
      .then(res => this.setState({ writings: res.data }))
      .catch(err => console.log(err))
  }



  render() {

    if (!this.state.writings) return null
    console.log(this.state.writings)

    return (
      <main>

        <div className="grid-container">

          {this.state.writings.map((writing, i) => (

            <div onMouseOver={this.colorChange}  key={i} className ="writing">

              <Link to={`/writings/${writing.id}`}>
                <span key={writing.id}><h3 key={writing.id}> {writing.text}</h3></span>
              </Link>
            </div>

          ))}

        </div>



      </main>
    )
  }
}

export default WritingsIndex
