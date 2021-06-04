//Greg Quinn
//1125128
import React from "react";
import ReactDOM from 'react-dom';
import PastPurchases from "./PastPurchases";
import renderer from 'react-test-renderer';

it("renders without crashing", () => {
    const div = document.createElement("div");
    ReactDOM.render(
    <PastPurchases />,
  div
    );
    ReactDOM.unmountComponentAtNode(div);
  })
  it('matches the snapshot', () => {
    
    const tree = renderer.create(<PastPurchases />).toJSON();
    expect(tree).toMatchSnapshot();
  });