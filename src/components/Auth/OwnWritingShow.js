import React from 'react'
import axios from 'axios'


import OwnEditsShow from './OwnEditsShow'


class OwnWritingShow extends React.Component {
  constructor() {
    super()

    this.state = {  edits: null, finals:null, filteredEdits: null }
    this.filterFinals = this.filterFinals.bind(this)



  }

  getFinals() {
    axios.get('/api/finals')
      .then(res => this.setState({ finals: res.data }, () => this.filterFinals()))
      .catch(err => console.log(err))
  }

  filterFinals() {
    let filtered = this.state.edits.map(edit => this.state.finals.filter(final =>

      (final.edit.id !== edit.id)

    ))[0]
    console.log(filtered)
    this.setState({ filteredEdits: filtered })

  }

  getEdits() {
    const edits = []
    axios.get(`/api/writings/${this.props.writing.id}/edits`)

      .then(res => this.setState({ edits: edits.concat(res.data) }, () => this.getFinals()))
      .catch(err => console.log(err))

  }



  componentDidMount() {
  this.getEdits()

  }




  render() {
    // if (!this.state.edits) return null
    if (!this.props.writing) return null
    if (!this.state.finals) return null
    if (!this.state.filteredEdits) return null
    if (!this.state.edits) return null
console.log('me!', this.state.finals)

    // this.diff('human', 'humat')
    return (

      <main>
        <div className="writingcontainer">


          <h2 className="writingTitle">{this.props.writing.title}</h2>

          <p key={this.props.writing.id} > {this.props.writing.text}</p>

          {this.state.filteredEdits &&
          <OwnEditsShow edits={this.state.edits} writing={this.props.writing}/>}


        </div>


      </main>

    )
  }
}

export default OwnWritingShow
