import React from 'react'
import axios from 'axios'


import OwnEditsShow from './OwnEditsShow'


class OwnWritingShow extends React.Component {
  constructor() {
    super()

    this.state = {  edits: null }



  }




  componentDidMount() {
    const edits = []
    // axios.get(`/api/writings/${this.props.match.params.id}`)
    //   .then(res => this.setprops({ writing: res.data }))
    //   .catch(err => console.log(err))
    axios.get(`/api/writings/${this.props.writing.id}/edits`)

      .then(res => this.setState({ edits: edits.concat(res.data) }))
      .catch(err => console.log(err))
  }




  render() {
    if (!this.state.edits) return null
    if (!this.props.writing) return null


    console.log('edits', this.props.edits)
    console.log(typeof this.props.edits)
    // this.diff('human', 'humat')


    return (

      <main>
        <div className="writingcontainer">


          <h2 className="writingTitle">{this.props.writing.title}</h2>

          <p key={this.props.writing.id} > {this.props.writing.text}</p>

          {this.state.edits &&
          <OwnEditsShow edits={this.state.edits} writing={this.props.writing}/>}


        </div>


      </main>

    )
  }
}

export default OwnWritingShow
