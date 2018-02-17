import BaseModel from '@/components/common/model/BaseModel'

class RiskModel extends BaseModel {
  defineEndPointURI () {
    return 'risk/'
  }

  getRisksByRiskType (pRiskTypeId) {
    return new Promise((resolve, reject) => {
      this._request.get(this.defineEndPointURI() + 'list-by-risk-type/', {risk_type_id: pRiskTypeId}).then((response) => {
        resolve(response)
      }).catch((pErr) => {
        reject(pErr)
      })
    })
  }
}
export default new RiskModel()
