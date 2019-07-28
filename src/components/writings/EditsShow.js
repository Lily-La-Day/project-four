import React from 'react'
import axios from 'axios'

// import { Link } from 'react-router-dom'
import EditRate from './EditRate'





class EditsShow extends React.Component {
  constructor() {
    super()

    this.state = { edits: [] , num: 0 }
    this.addOne = this.addOne.bind(this)
    this.minusOne = this.minusOne.bind(this)


  }

  addOne() {
    let number = this.state.num
    number += 1
    this.setState({ num: number })
  }



  minusOne() {
    let number = this.state.num
    number -= 1
    this.setState({ num: number })
  }




  render() {

    if (!this.props.edits) return null
    if(!this.props)

      console.log(this.props.edits)
    console.log(typeof this.props.edits)
    // this.diff('human', 'humat')


    return (
      <main>
        <div className="edit-snippet-section">
          {this.props.edits.map((edit, i) => (
            <div key={i}>
              { (this.state.num === i) &&
              <EditRate edit={edit} writing={this.props.writing}/> }

            </div>

          ))}
          <button onClick={this.addOne} className="show-button">Next edit</button>
          <button onClick={this.minusOne}  className="show-button">Last edit</button>


        </div>









      </main>

    )
  }
}

export default EditsShow
