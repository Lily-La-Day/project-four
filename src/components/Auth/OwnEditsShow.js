import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import FinalShow from './FinalShow'

// import { Link } from 'react-router-dom'






class OwnEditsShow extends React.Component {
  constructor() {
    super()

    this.state = {  num: 0, final: null, confirmation: false }
    this.addOne = this.addOne.bind(this)
    this.minusOne = this.minusOne.bind(this)
    this.selectFinal = this.selectFinal.bind(this)
    this.confirmFinal = this.confirmFinal.bind(this)


  }

  addOne() {
    let number = this.state.num
    number += 1
    this.setState({ num: number })
  }

  minusOne() {
    let number = this.state.num
    number -= 1
    this.setState({ num: number })
  }

  selectFinal(edit) {

    this.setState({ final: edit })
    console.log(edit)

  }

  confirmFinal() {
    this.setState({ confirmation: true })
    this.postFinal()
  }



  postFinal() {
    console.log(this.state.final)
    axios.post('/api/finals', this.state.final,  {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}


    })
      .catch((err) => console.log(err))

  }








  render() {

    if (!this.props.edits) return null
    if(!this.props)

      console.log(this.state.final)
    return (
      <main>
        {!this.state.confirmation && <div className="edit-snippet-section">
          {this.props.edits.map((edit, i) => (
            <div key={i}>
              {(this.state.num === i) &&
                <section className="own-edits">
                  <h4>{edit.title}</h4>
                  <h6>{edit.text}</h6>
                  {edit.rating && <h2>{edit.rating}</h2>}

                </section>



              }

              {!this.state.final && <button onClick={() => this.selectFinal(edit)}>Make Final</button>}
              {this.state.final && <button onClick={() => this.confirmFinal(edit)}>Are you sure!? Once you confirm
            it is confirmed!</button>}

            </div>

          ))}

          <button onClick={this.addOne}>Next Edit</button>
          <button onClick={this.minusOne}>Last Edit</button>

        </div>}
        {this.state.confirmation && <FinalShow edit={this.state.final}/>}















      </main>

    )
  }
}

export default OwnEditsShow
