import React from 'react'
// import axios from 'axios'
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
    console.log('bagus sekali')
    return (
      <main>
        <div className="edit-snippet-section">

          {this.props.edits.map((edit, i) => (
            <div key={i}>
              { (this.state.num === i) &&
              <EditRate edit={edit} writing={this.props.writing}/> }

            </div>

          ))}

          {this.state.num < this.props.edits.length && <button onClick={this.addOne} className="show-button">Next edit</button>}

          {this.state.num > 0 && <button onClick={this.minusOne}  className="show-button">Last edit</button>}

        </div>











      </main>

    )
  }
}

export default EditsShow
