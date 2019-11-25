import { mount } from '@vue/test-utils'
import { shallow } from '@vue/test-utils'
import UserPage from '../src/views/UserPage.vue'
import CalendarPage from '../src/views/CalendarPage.vue'

describe('UserPage.vue', () => {
    it("Password Match", () => {
        const wrapper = mount(UserPage)
        wrapper.setData({pw: "asdf"})
        wrapper.setData({retypePassword: "asdf"});

        expect(wrapper.vm.passwordMatch()).toBe('')
    })
    it("Password mismatch", () => {
        const wrapper = mount(UserPage);
        wrapper.setData({pw: 'asdf'})
        expect(wrapper.vm.passwordMatch()).toBe('Mismatched Password')
    })

    it("Creating User", () => {
        const wrapper = shallow(UserPage, {
            stubs: {
                form: { 
                  render(g) { return h('div') },
                  methods: {
                    validate() {}
                  }
                }
              }
        });
        wrapper.setData({email1: "test@gmail.com", password: "123", name1: "test", retypePassword: "123"});
        expect(wrapper.vm.createUser()).toBe("200")
    })
})

describe('CalendarPage.vue', () => {
    it("Get Date", () => {
        const wrapper = mount(CalendarPage);

       
    })
})