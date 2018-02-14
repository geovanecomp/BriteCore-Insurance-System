import BaseRequest from './BaseRequest'

export default class BaseModel {
  constructor () {
    this._endPointURI = this.defineEndPointURI()
    this._request = this.defineRequest()
  }

  isModel () {
    return true
  }

  defineEndPointURI () {
    throw new Error('You need to provide a URI to the Model')
  }

  defineRequest () {
    let request = BaseRequest.getInstance()

    return request
  }

  defineRequestConfig () {
    return {}
  }

  find (id, filter = {}) {
    // eslint-disable-next-line
    if (!id) return Promise.reject({error: 'Id is needed'})
    const findURL = this._endPointURI + '/' + id
    return this._request.get(findURL, filter).then((response) => {
      return response
    })
  }

  update (id, formData) {
    return this._request.put(`${this._endPointURI}/${id}`, formData).then((response) => {
      return response
    })
  }

  remove (id) {
    return this._request.delete(`${this._endPointURI}/${id}`).then((response) => {
      return response
    })
  }

  create (formData) {
    return this._request.post(this._endPointURI, formData).then((response) => {
      return response
    })
  }

  search (filter = {}) {
    return this._request.get(this._endPointURI, filter).then((response) => {
      return response
    })
  }
}
