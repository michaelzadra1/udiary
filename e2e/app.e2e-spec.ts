import { UdiaryPage } from './app.po';

describe('udiary App', function() {
  let page: UdiaryPage;

  beforeEach(() => {
    page = new UdiaryPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
