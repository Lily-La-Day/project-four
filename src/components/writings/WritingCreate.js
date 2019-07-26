import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'





class WritingCreate extends React.Component {
  constructor() {
    super()

    this.state = { data: { } }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)


  }

  handleChange({ target: { name, value }}) {

    const data = {...this.state.data, [name]: value }

    this.setState({ data, error: ''})


  }

  handleSubmit(e) {
    e.preventDefault()
    console.log(this.state.data)
    axios.post('/api/writings', this.state.data,  {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })

      .then(() => {

        this.props.history.push('/writings')
      })
      .catch((err) => console.log(err))
  }




  render() {

    console.log(this.state.data)
    // this.diff('human', 'humat')


    return (
      <main>

        <form className="form-style" onSubmit={this.handleSubmit} >

          <h3>Submit Some Writing</h3>

          <label className='label'>Title</label>
          <div className="control">
            <input
              onChange = {this.handleChange}
              className="input"
              name="title"

              placeholder='The Title/Name of your Writing Here'/>
          </div>
          <label className='label'>Your Writing</label>
          <div className="control">
            <textarea 
              onChange = {this.handleChange}
              type="text"
              className="submit-writing input"
              name="text"
              placeholder='Paste you writing here'
              lines='150'
            />
          </div>

          <button type="submit" className="button" > Submit your writing. </button>


        </form>
      </main>

    )
  }
}

export default WritingCreate
