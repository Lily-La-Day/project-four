import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

const Diff = require('diff')



class EditCreate extends React.Component {
  constructor() {
    super()

    this.state = { writing: null, data: { } }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)


  }

  handleChange({ target: { name, value }}) {

    const data = {...this.state.data, [name]: value, original: { id: this.state.writing.id } }

    this.setState({ data, error: ''})


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
    axios.get(`/api/writings/${this.props.match.params.id}`)
      .then(res => this.setState({ writing: res.data, original: { id: res.data.id } }))
      .catch(err => console.log(err))

  }

  diff(oldStr, newStr){
    console.log(Diff.diffChars(oldStr, newStr))
  }


  render() {
    if (!this.state.writing) return null
    console.log(this.state.writing)
    // this.diff('human', 'humat')
    const { writing } =  this.state

    return (
      <main>
        <div className="edit-container">
          <div className ="original">
            <h2 className="original-title">{writing.title}</h2>



            <h5 key={writing.id}> {writing.text}</h5>

          </div>


          <form className="form-style create-edit" onSubmit={this.handleSubmit} >

            <h3>Submit an Edit</h3>

            <label className='label'>Title</label>
            <div className="control">
              <input
                onChange = {this.handleChange}
                className="input"
                name="title"

                defaultValue={this.state.writing.title}/>
            </div>
            <label className='label'>Your Edit</label>
            <div className="control">
              <textarea
                onChange = {this.handleChange}
                type="text"
                className="submit-writing input"
                name="text"
                defaultValue= {this.state.writing.text}
              />
            </div>


            <button type="submit" className="button" > Submit your edit. </button>


          </form>
        </div>
      </main>

    )
  }
}

export default EditCreate
