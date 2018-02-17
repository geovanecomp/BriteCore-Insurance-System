import BaseModel from '@/components/common/model/BaseModel'

class RiskModel extends BaseModel {
  defineEndPointURI () {
    return 'risk/'
  }

  getRisksByRiskType (pRiskTypeId) {
    const riskByTypeUri = this.defineEndPointURI() + 'list-by-risk-type/'
    return new Promise((resolve, reject) => {
      this._request.get(riskByTypeUri, {risk_type_id: pRiskTypeId}).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }

  getFieldsByRisk (pRiskId) {
    const fieldByRiskUri = 'fields-by-risk/list-fields-by-risk/'
    return new Promise((resolve, reject) => {
      this._request.get(fieldByRiskUri, {risk_id: pRiskId}).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }
}

export default new RiskModel()
