import React from 'react'
import axios from 'axios'


import OwnEditsShow from './OwnEditsShow'


class OwnWritingShow extends React.Component {
  constructor() {
    super()

    this.state = {  edits: null, finals: null, filteredEdits: null }
    this.filterFinals = this.filterFinals.bind(this)
  }

  getFinals() {
    axios.get('/api/finals')
      .then(res => this.setState({ finals: res.data }, () => this.filterFinals()))
      .catch(err => console.log(err))
  }

  filterFinals() {
    const filtered = this.state.edits.map(edit => edit.id)
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

    if (!this.props.writing) return null


    return (
      <main>
        <div className="writingcontainer">
          <h6 className="subtitle"> Your writing...</h6>
          <h3 className="writingTitle">{this.props.writing.title}</h3>
          <p key={this.props.writing.id} > {this.props.writing.text}</p>
          {this.state.edits && this.state.filteredEdits &&
          <OwnEditsShow edits={this.state.edits}
            writing={this.props.writing}
            finals={this.state.finals}/>}
        </div>
      </main>

    )
  }
}

export default OwnWritingShow
