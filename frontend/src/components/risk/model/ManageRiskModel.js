import BaseModel from '@/components/common/model/BaseModel'

class ManageRiskModel extends BaseModel {
  defineEndPointURI () {
    return 'risk/'
  }

  createRisk (pObj) {
    return new Promise((resolve, reject) => {
      this._request.post(this.defineEndPointURI(), pObj).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  createField (pObj) {
    const fieldUri = 'field/'
    return new Promise((resolve, reject) => {
      this._request.post(fieldUri, pObj).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  createFieldsByRisk (pRiskId, pObjs) {
    const fieldsByRiskUri = 'fields-by-risk/'
    let preparedObj = pObjs[0]
    preparedObj.risk = pRiskId
    preparedObj.field = pObjs[0].fieldType
    console.log(pRiskId, pObjs[0], preparedObj)
    return new Promise((resolve, reject) => {
      this._request.post(fieldsByRiskUri, preparedObj).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  deleteRisk (pId) {
    return new Promise((resolve, reject) => {
      this._request.delete(this.defineEndPointURI() + pId + '/').then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  updateRisk (pId, pObj) {
    return new Promise((resolve, reject) => {
      this._request.put(this.defineEndPointURI() + pId + '/', pObj).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  getAllFieldTypes () {
    const fieldTypeUri = 'field-types/'
    return new Promise((resolve, reject) => {
      this._request.get(fieldTypeUri).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }
}
export default new ManageRiskModel()
