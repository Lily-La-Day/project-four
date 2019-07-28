import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

const Diff = require('diff')



class EditCreate extends React.Component {
  constructor() {
    super()

    this.state = { writing: null, data: { }, text: [] }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.makeArray = this.makeArray.bind(this)


  }

  handleChange({ target: { name, value }}) {

    const data = {...this.state.data, [name]: value, original: { id: this.state.writing.id } }

    this.setState({ data, error: ''})


  }

  print() {
    console.log('working')
  }

  // makeArray(e) {
  //   const text = [e.target.value.split(' ')]
  //   console.log(typeof text)
  //   const textArray = text[0]
  //   textArray.map((word) => {
  //     const span = document.createElement('span')
  //
  //     span.textContent = word
  //     console.log(word)
  //     console.log(word.length)
  //
  //
  //
  //   })
  //   console.log()
  //   console.log(event.target.selectionStart)
  //
  // }

  makeArray() {

    const text = [this.state.writing.text.split(' ')][0]

    text.map((word) => {
      const span = document.createElement('span')

      span.textContent = `${word} `
      word = span
      console.log(word)





    })

    this.setState({ text: text })

    // console.log()
    // console.log(event.target.selectionStart)

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



    // this.diff('human', 'humat')
    const { writing } =  this.state

    return (
      <main onClick={(e) => console.log(e.target)}>
        <div className="edit-container">
          <div className ="original">
            <h2 className="original-title">{writing.title}</h2>



            <h5 key={writing.id}> {writing.text}</h5>

          </div>

          {this.state.text.map(word => <p>{word}</p>)}
          <form className="form-style create-edit" onSubmit={this.handleSubmit}  >

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
                onMouseOver={this.makeArray}
                defaultValue= {this.state.text}
                onClick = {(e) => console.log(e.target.value)}


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
