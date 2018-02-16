import axios from 'axios'
import serverConfig from '../../../config.js'

let _instance = null

export default class BaseRequest {
  constructor (config = null) {
    this._config = config || this.defineBaseConfig()

    if (!this._config) {
      throw new Error('You need to provide a config via constructor or something is wrong on Request defineBaseConfig')
    }
    this._axios = axios.create(Object.assign({}, this._config, config))
  }

  defineBaseConfig (config) {
    return serverConfig
  }

  static getInstance () {
    if (!_instance) {
      _instance = new BaseRequest()
    }
    return _instance
  }

  get (url, data = {}) {
    return this._send(url, 'GET', data)
  }

  post (url, data = {}) {
    return this._send(url, 'POST', data)
  }

  put (url, data = {}) {
    return this._send(url, 'PUT', data)
  }

  delete (url, data = {}) {
    return this._send(url, 'DELETE', data)
  }

  option (url, data = {}) {
    return this._send(url, 'OPTION', data)
  }

  _send (url, method = 'GET', data = {}) {
    let promise = this._axios.request({
      url,
      method,
      headers: this._getHeaders(),
      params: method === 'GET' ? data : null,
      data: method !== 'GET' ? data : null
    })
    return this._prepareResponse(promise)
  }

  _getHeaders () {
    let headers = {}
    headers['Content-Type'] = 'application/json'
    return headers
  }

  _prepareResponse (promise) {
    promise.then((response) => { this._handleSuccessResponse(response) })
      .catch((error) => { this._handleErrorResponse(error) })
    return promise
  }

  _handleSuccessResponse (response) {
    if (response.data.data) {
      response.data = response.data.data
    }
    return response
  }

  _handleErrorResponse (error) {
    if (!error.response) {
      return this._noResponse(error)
    }

    if (error.response.data.errors) {
      error.response.errors = error.response.data.errors
      delete error.response.data
    }

    let httpStatus = error.response.status
    switch (httpStatus) {
      // TODO: Filter by http status
    }
    return error.response
  }

  _noResponse (error) {
    return error
  }
}
