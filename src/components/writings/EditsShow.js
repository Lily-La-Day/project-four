import React from 'react'
import axios from 'axios'
// import Auth from '../../lib/Auth'
// import { Link } from 'react-router-dom'





class EditsShow extends React.Component {
  constructor() {
    super()

    this.state = { edits: [] }



  }




  componentDidMount() {
    const edits = []

    axios.get(`/api/writings/${this.props.match.params.id}/edits`)

      .then(res => this.setState({ edits: edits.concat(res.data) }))
      .catch(err => console.log(err))
  }




  render() {

    if (!this.state.edits) return null

    console.log(this.state.edits)
    console.log(typeof this.state.edits)
    // this.diff('human', 'humat')


    return (
      <main>
        <div className="edit-snippet-section">
          {this.state.edits.map((edit, i) => (
            <div key={i} >
              {/* <h2 className="writingTitle">{this.state.edit.title}</h2> */}
              <h5 key={i} className="edit-snippet"> {edit.text}</h5>
              <div className="content">
                <h3>Rate This Edit</h3>
                <span><i className="fa fa-star"></i></span>

              </div>

              <div className="wrapper">
                <input type="checkbox" id="st1" value="1" />
                <label htmlFor="st1"></label>
                <input type="checkbox" id="st2" value="2" />
                <label htmlFor="st2"></label>
                <input type="checkbox" id="st3" value="3" />
                <label htmlFor="st3"></label>
                <input type="checkbox" id="st4" value="4" />
                <label htmlFor="st4"></label>
                <input type="checkbox" id="st5" value="5" />
                <label htmlFor="st5"></label>
              </div>
            </div>

          ))}

        </div>






      </main>

    )
  }
}

export default EditsShow
