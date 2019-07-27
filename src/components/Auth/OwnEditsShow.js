import React from 'react'
import axios from 'axios'

// import { Link } from 'react-router-dom'






class OwnEditsShow extends React.Component {
  constructor() {
    super()

    this.state = {  num: 0 }
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

      console.log(this.state.edits)
    console.log(typeof this.state.edits)
    // this.diff('human', 'humat')


    return (
      <main>
        <div className="edit-snippet-section">
          {this.props.edits.map((edit, i) => (
            <div key={i}>
              {(this.state.num === i) &&
                <section className="own-edits">
                  <h4>{edit.title}</h4>
                  <h6>{edit.text}</h6>

                </section>



              }


            </div>
          ))}
          <button onClick={this.makeFinal}>Make Final</button>
          <button onClick={this.addOne}>Next Edit</button>
          <button onClick={this.minusOne}>Last Edit</button>

        </div>













      </main>

    )
  }
}

export default OwnEditsShow
