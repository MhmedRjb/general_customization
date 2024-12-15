function overridePOSItemCart() {
  if (
    typeof erpnext !== "undefined" &&
    typeof erpnext.PointOfSale !== "undefined" &&
    typeof erpnext.PointOfSale.ItemCart !== "undefined"
  ) {

    erpnext.PointOfSale.ItemCart.prototype.toggle_customer_info = function (
      show
    ) {
      if (show) {
        const { customer } = this.customer_info || {};

        this.$cart_container.css("display", "none");
        this.$customer_section.css({
          height: "100%",
          "padding-top": "0px",
        });
        this.$customer_section.find(".customer-details").html(
          `<div class="header">
					<div class="label">${__("Contact Details")}</div>
					<div class="close-details-btn">
						<svg width="32" height="32" viewBox="0 0 14 14" fill="none">
							<path d="M4.93764 4.93759L7.00003 6.99998M9.06243 9.06238L7.00003 6.99998M7.00003 6.99998L4.93764 9.06238L9.06243 4.93759" stroke="#8D99A6"/>
						</svg>
					</div>
				</div>
				<div class="customer-display">
					${this.get_customer_image()}
					<div class="customer-name-desc">
						<div class="customer-name">${customer}</div>
						<div class="customer-desc"></div>
					</div>
				</div>
				<div class="customer-fields-container">
			

				
					<div class="email_id-field"></div>
					<div class="mobile_no-field"></div>
					<div class="loyalty_program-field"></div>
					<div class="loyalty_points-field"></div>


	<div class="total_unpaid-field-container" style="margin-bottom: 10px;">
    <div class="total_unpaid-label" style="font-weight: bold; margin-bottom: 5px;">${__(
      "Total Unpaid"
    )}</div>
    <div class="total_unpaid-field input-xs" 
         style="border: 1px solid var(--gray-300); padding: 5px; border-radius: 6px; background-color: #f9f9f9; font-size: 14px; min-height: 30px; color: #333; opacity: 0.6; pointer-events: none;">0.00</div>
    </div>
				</div>
				<div class="transactions-label">${__("Recent Transactions")}</div>`
        );
        // transactions need to be in diff div from sticky elem for scrolling
        this.$customer_section.append(
          `<div class="customer-transactions"></div>`
        );

        this.render_customer_fields();
        this.fetch_customer_transactions();
      } else {
        this.$cart_container.css("display", "flex");
        this.$customer_section.css({
          height: "",
          "padding-top": "",
        });

        this.update_customer_section();
      }
    };

    erpnext.PointOfSale.ItemCart.prototype.update_total_unpaid = function (
      customer
    ) {
      const me = this;

      frappe.call({
        method: "erpnext.accounts.utils.get_balance_on",
        args: {
          party_type: "Customer",
          party: customer,
        },
        callback: function (r) {
          if (r.message) {
            var total = r.message;
            console.log(r.message);
            console.log("dom", me.$component.find(".total_unpaid-field")); // Check if the element is found
            me.$component.find(".total_unpaid-field").text(total);
            console.log("the customer is", customer);
            console.log("the amount is", r.message);
          } else {
          }
        },
      });

    };

  } else {
    setTimeout(overridePOSItemCart, 100);
  }
}
overridePOSItemCart();
