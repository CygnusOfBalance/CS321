import { mount } from '@vue/test-utils'
import LoginPage from '../src/views/loginPage.vue'

describe('loginPage.vue', () => {
    it("Reset validation", () => {
        const wrapper = mount(LoginPage);
        wrapper.setData({pw: 'asdf'})
        wrapper.vm.reset()
        expect(wrapper.vm.pw).toBe('')
    })
})