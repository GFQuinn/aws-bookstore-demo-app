//Greg Quinn
//1125128
import React from "react";
import Enzyme from 'enzyme';
import { shallow } from 'enzyme';
import BestSellers from "./BestSellers";
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({ adapter: new Adapter() });


 test("Heading is = Top 20 best sellers", () => {
const wrapper = shallow(<BestSellers/>)
return expect(wrapper.find('h3').text()).toEqual('Top 20 best sellers');
  });