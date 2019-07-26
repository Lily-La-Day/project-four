import React, { Component } from 'react'
import axios from 'axios'




class Search extends React.Component {
  constructor() {
    super()
    this.state = {
      query: '',
      category: 0,
      writings: []

    }
    this.handleInputChange = this.handleInputChange.bind(this)
  }

  getInfo () {
    console.log(this.state.category)
    axios.get(`/api/categories/${this.state.category}`)
      .then((res) => {
        this.setState({
          writings: res.data
        })
      })
  }

  setCategory(data) {
    switch(data) {
      case 'romantic':
        this.setstate({
          category: 1
        })
        break
      case 'personal':
        this.setstate({
          category: 2
        })
        break
      case 'business':
        this.setstate({
          category: 3
        })
        break
      case 'formal':
        this.setstate({
          category: 4
        })
        break
      case 'letters of complaint':
        this.setstate({
          category: 5
        })
        break
      case 'work':
        this.setstate({
          category: 6
        })
        break
      case 'cover letter':
        this.setstate({
          category: 7
        })
        break
      case 'cv':
        this.setstate({
          category: 8
        })
        break
      case 'family':
        this.setstate({
          category: 9
        })
        break
      case 'thank you':
        this.setstate({
          category: 10
        })
        break
      case 'application':
        this.setstate({
          category: 11
        })
        break
      case 'feedback':
        this.setstate({
          category: 12
        })
        break
      case 'prose':
        this.setstate({
          category: 13
        })
        break
      case 'short story':
        this.setstate({
          category: 14
        })
        break
      case 'obituary':
        this.setstate({
          category: 15
        })
        break
      case 'journalism':
        this.setstate({
          category: 16
        })
        break
      case 'poetry':
        this.setstate({
          category: 17
        })
        break
      case 'formal communication':
        this.setstate({
          category: 18
        })
        break
      case 'enquiry':
        this.setstate({
          category: 19
        })
        break
      case 'suggestion':
        this.setstate({
          category: 20
        })
        break
      case 'criticism':
        this.setstate({
          category: 21
        })
        break
      case 'blog':
        this.setstate({
          category: 22
        })
        break
      case 'fan fiction':
        this.setstate({
          category: 23
        })
        break
      case 'appreciation':
        this.setstate({
          category: 24
        })
        break
      case 'branding':
        this.setstate({
          category: 25
        })
        break
      case 'press release':
        this.setstate({
          category: 26
        })
        break

    }

  }

  handleInputChange(e) {
    e.preventDefault()

    console.log(this.state.query, this.state.category)
    this.setState({
      query: this.search.value
    }, () => {
      if (this.state.query && this.state.query.length > 1) {
        if (this.state.query.length % 2 === 0) {
          this.setCategory(this.state.query)
          this.getInfo()


        }
      }
    })
  }

  render() {
    console.log(this.state.writings)
    return (
      <form>
        <input
          placeholder="Search writing categories..."
          ref={input => this.search = input}
          onChange={this.handleInputChange}
        />
        <p>{this.state.query}</p>
      </form>
    )
  }
}

export default Search
