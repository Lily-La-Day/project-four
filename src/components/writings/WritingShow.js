import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import { Link } from 'react-router-dom'





class WritingShow extends React.Component {
  constructor() {
    super()

    this.state = { writing: null, edits: [] }



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


  componentDidMount() {
    const edits = []
    axios.get(`/api/writings/${this.props.match.params.id}`)
      .then(res => this.setState({ writing: res.data }))
      .catch(err => console.log(err))
    axios.get(`/api/writings/${this.props.match.params.id}/edits`)

      .then(res => this.setState({ edits: edits.concat(res.data) }))
      .catch(err => console.log(err))
  }




  render() {
    if (!this.state.writing) return null
    if (!this.state.edits) return null

    console.log(this.state.edits)
    console.log(typeof this.state.edits)
    // this.diff('human', 'humat')


    return (
      <main>
        <div className="writingcontainer">

          <h2 className="writingTitle">{this.state.writing.title}</h2>

          <p key={this.state.writing.id} > {this.state.writing.text}</p>

          <Link to={`/writings/${this.state.writing.id}/edit`}> <button className="edit-button"> Edit </button></Link>




          <Link to={`/writings/${this.state.writing.id}/edits`}>
            <button className="edits-button"> See Submitted Edits </button>
          </Link>

        </div>


      </main>

    )
  }
}

export default WritingShow
