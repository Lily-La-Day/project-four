import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import { Link } from 'react-router-dom'
import EditsShow from './EditsShow'





class WritingShow extends React.Component {
  constructor() {
    super()

    this.state = { writing: null, edits: null, seeTheEdits: false }

    this.seeEdit = this.seeEdit.bind(this)


  }



  handleSubmit(e) {
    e.preventDefault()
    console.log(this.state.data)
    axios.post('/api/edits', this.state.data,  {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })

      .then(() => {

        this.props.history.push('/writings')
      })
      .catch((err) => console.log(err))
  }


  seeEdit() {
    this.setState({ seeTheEdits: true })
    console.log(this.see)
  }


  componentDidMount() {

    axios.get(`/api/writings/${this.props.match.params.id}`)
      .then(res => this.setState({ writing: res.data }))
      .catch(err => console.log(err))
    this.getEdits()

  }

  getEdits() {
    const edits = []
    axios.get(`/api/writings/${this.props.match.params.id}/edits`)

      .then(res => this.setState({ edits: edits.concat(res.data) }))
      .catch(err => console.log(err))
  }




  render() {
    if (!this.state.writing) return null


    console.log('edits', this.state.edits)
    console.log(typeof this.state.edits)
    // this.diff('human', 'humat')


    return (

      <main>
        {!this.state.seeTheEdits && <div className="writingcontainer">


      <h2 className="writingTitle">{this.state.writing.title}</h2>

          <p  className="writing-show" key={this.state.writing.id} > {this.state.writing.text}</p>

          <Link to={`/edit-writings/${this.state.writing.id}/edit`}> <button className="edit-button"> Edit </button></Link>

  </div>}
  <div className="show-edit-container">
          {this.state.edits && !this.state.seeTheEdits &&  <button onClick={this.seeEdit} className="show-button"> See Submitted Edits </button>}

          {this.state.seeTheEdits && <EditsShow edits={this.state.edits} writing={this.state.writing}/>}



      </div>


      </main>

    )
  }
}

export default WritingShow
