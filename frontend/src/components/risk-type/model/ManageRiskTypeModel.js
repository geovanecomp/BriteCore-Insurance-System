import BaseModel from '@/components/common/model/BaseModel'

class ManageRiskTypeModel extends BaseModel {
  defineEndPointURI () {
    return 'risk-types/'
  }

  getAllRiskTypes () {
    return new Promise((resolve, reject) => {
      this._request.get(this.defineEndPointURI()).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  createRiskType (pObj) {
    return new Promise((resolve, reject) => {
      this._request.post(this.defineEndPointURI(), pObj).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  deleteRiskType (pId) {
    return new Promise((resolve, reject) => {
      this._request.delete(this.defineEndPointURI() + pId + '/').then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  updateRiskType (pId, pObj) {
    return new Promise((resolve, reject) => {
      this._request.put(this.defineEndPointURI() + pId + '/', pObj).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }
}
export default new ManageRiskTypeModel()
