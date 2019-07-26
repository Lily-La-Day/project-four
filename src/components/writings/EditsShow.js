import React from 'react'
import axios from 'axios'

// import { Link } from 'react-router-dom'
import EditRate from './EditRate'





class EditsShow extends React.Component {
  constructor() {
    super()

    this.state = { edits: [] , num: 0 }
    this.addOne = this.addOne.bind(this)


  }

  addOne() {
    let number = this.state.num
    number += 1
    this.setState({ num: number })
  }




  componentDidMount() {
    const edits = []

    axios.get(`/api/writings/${this.props.match.params.id}/edits`)

      .then(res => this.setState({ edits: edits.concat(res.data) }))
      .catch(err => console.log(err))
  }



  render() {

    if (!this.state.edits) return null
    if(!this.props)

      console.log(this.state.edits)
    console.log(typeof this.state.edits)
    // this.diff('human', 'humat')


    return (
      <main>
        <div className="edit-snippet-section">
          {this.state.edits.map((edit, i) => (
            <div key={i}>
              { (this.state.num === i) &&
              <EditRate edit={edit} writing={this.props.match.params.id}/> }

            </div>

          ))}
          <button onClick={this.addOne}>Next edit</button>



        </div>









      </main>

    )
  }
}

export default EditsShow
