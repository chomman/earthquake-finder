/**
 * form_button.js: this file contains functions related to form button elements.
 */

/**
 * close_result: removes the html container containing results generated from the
 *               server.
 */
  var close_result = function() {
    $('body').on('click', '.close-result', function() {
      $('.result-container').remove();
      $('.close-result').remove();
    });
  }

/**
 * constructor
 */
  $(function() {
    var closed_result = new close_result();
  });
