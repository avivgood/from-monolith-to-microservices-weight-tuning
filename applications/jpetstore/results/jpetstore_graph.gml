<?xml version='1.0' encoding='utf-8'?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key id="d3" for="edge" attr.name="rel_type" attr.type="string" />
  <key id="d2" for="node" attr.name="class_name" attr.type="string" />
  <key id="d1" for="node" attr.name="type" attr.type="string" />
  <key id="d0" for="node" attr.name="name" attr.type="string" />
  <graph edgedefault="directed">
    <node id="0">
      <data key="d0">Category</data>
      <data key="d1">Entity</data>
    </node>
    <node id="1">
      <data key="d0">Item</data>
      <data key="d1">Entity</data>
    </node>
    <node id="2">
      <data key="d0">LineItem</data>
      <data key="d1">Entity</data>
    </node>
    <node id="3">
      <data key="d0">Order</data>
      <data key="d1">Entity</data>
    </node>
    <node id="4">
      <data key="d0">Cart</data>
      <data key="d1">Entity</data>
    </node>
    <node id="5">
      <data key="d0">Product</data>
      <data key="d1">Entity</data>
    </node>
    <node id="6">
      <data key="d0">CartItem</data>
      <data key="d1">Entity</data>
    </node>
    <node id="7">
      <data key="d0">Account</data>
      <data key="d1">Entity</data>
    </node>
    <node id="8">
      <data key="d0">Sequence</data>
      <data key="d1">Entity</data>
    </node>
    <node id="9">
      <data key="d0">getCategoryList</data>
      <data key="d1">Method</data>
      <data key="d2">CategoryMapper</data>
    </node>
    <node id="10">
      <data key="d0">getCategory</data>
      <data key="d1">Method</data>
      <data key="d2">CategoryMapper</data>
    </node>
    <node id="11">
      <data key="d0">getProductListByCategory</data>
      <data key="d1">Method</data>
      <data key="d2">ProductMapper</data>
    </node>
    <node id="12">
      <data key="d0">getProduct</data>
      <data key="d1">Method</data>
      <data key="d2">ProductMapper</data>
    </node>
    <node id="13">
      <data key="d0">searchProductList</data>
      <data key="d1">Method</data>
      <data key="d2">ProductMapper</data>
    </node>
    <node id="14">
      <data key="d0">getOrdersByUsername</data>
      <data key="d1">Method</data>
      <data key="d2">OrderMapper</data>
    </node>
    <node id="15">
      <data key="d0">getOrder</data>
      <data key="d1">Method</data>
      <data key="d2">OrderMapper</data>
    </node>
    <node id="16">
      <data key="d0">insertOrder</data>
      <data key="d1">Method</data>
      <data key="d2">OrderMapper</data>
    </node>
    <node id="17">
      <data key="d0">insertOrderStatus</data>
      <data key="d1">Method</data>
      <data key="d2">OrderMapper</data>
    </node>
    <node id="18">
      <data key="d0">getAccountByUsername</data>
      <data key="d1">Method</data>
      <data key="d2">AccountMapper</data>
    </node>
    <node id="19">
      <data key="d0">getAccountByUsernameAndPassword</data>
      <data key="d1">Method</data>
      <data key="d2">AccountMapper</data>
    </node>
    <node id="20">
      <data key="d0">insertAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountMapper</data>
    </node>
    <node id="21">
      <data key="d0">insertProfile</data>
      <data key="d1">Method</data>
      <data key="d2">AccountMapper</data>
    </node>
    <node id="22">
      <data key="d0">insertSignon</data>
      <data key="d1">Method</data>
      <data key="d2">AccountMapper</data>
    </node>
    <node id="23">
      <data key="d0">updateAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountMapper</data>
    </node>
    <node id="24">
      <data key="d0">updateProfile</data>
      <data key="d1">Method</data>
      <data key="d2">AccountMapper</data>
    </node>
    <node id="25">
      <data key="d0">updateSignon</data>
      <data key="d1">Method</data>
      <data key="d2">AccountMapper</data>
    </node>
    <node id="26">
      <data key="d0">getSequence</data>
      <data key="d1">Method</data>
      <data key="d2">SequenceMapper</data>
    </node>
    <node id="27">
      <data key="d0">updateSequence</data>
      <data key="d1">Method</data>
      <data key="d2">SequenceMapper</data>
    </node>
    <node id="28">
      <data key="d0">getLineItemsByOrderId</data>
      <data key="d1">Method</data>
      <data key="d2">LineItemMapper</data>
    </node>
    <node id="29">
      <data key="d0">insertLineItem</data>
      <data key="d1">Method</data>
      <data key="d2">LineItemMapper</data>
    </node>
    <node id="31">
      <data key="d0">getInventoryQuantity</data>
      <data key="d1">Method</data>
      <data key="d2">ItemMapper</data>
    </node>
    <node id="32">
      <data key="d0">getItemListByProduct</data>
      <data key="d1">Method</data>
      <data key="d2">ItemMapper</data>
    </node>
    <node id="33">
      <data key="d0">getItem</data>
      <data key="d1">Method</data>
      <data key="d2">ItemMapper</data>
    </node>
    <node id="34">
      <data key="d0">getCategoryList</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogService</data>
    </node>
    <node id="35">
      <data key="d0">getCategory</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogService</data>
    </node>
    <node id="36">
      <data key="d0">getProduct</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogService</data>
    </node>
    <node id="37">
      <data key="d0">getProductListByCategory</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogService</data>
    </node>
    <node id="38">
      <data key="d0">searchProductList</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogService</data>
    </node>
    <node id="39">
      <data key="d0">getItemListByProduct</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogService</data>
    </node>
    <node id="40">
      <data key="d0">getItem</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogService</data>
    </node>
    <node id="41">
      <data key="d0">isItemInStock</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogService</data>
    </node>
    <node id="42">
      <data key="d0">getAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountService</data>
    </node>
    <node id="43">
      <data key="d0">insertAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountService</data>
    </node>
    <node id="44">
      <data key="d0">updateAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountService</data>
    </node>
    <node id="45">
      <data key="d0">insertOrder</data>
      <data key="d1">Method</data>
      <data key="d2">OrderService</data>
    </node>
    <node id="46">
      <data key="d0">getOrder</data>
      <data key="d1">Method</data>
      <data key="d2">OrderService</data>
    </node>
    <node id="47">
      <data key="d0">getOrdersByUsername</data>
      <data key="d1">Method</data>
      <data key="d2">OrderService</data>
    </node>
    <node id="48">
      <data key="d0">getNextId</data>
      <data key="d1">Method</data>
      <data key="d2">OrderService</data>
    </node>
    <node id="49">
      <data key="d0">getCart</data>
      <data key="d1">Method</data>
      <data key="d2">CartActionBean</data>
    </node>
    <node id="50">
      <data key="d0">setCart</data>
      <data key="d1">Method</data>
      <data key="d2">CartActionBean</data>
    </node>
    <node id="52">
      <data key="d0">addItemToCart</data>
      <data key="d1">Method</data>
      <data key="d2">CartActionBean</data>
    </node>
    <node id="53">
      <data key="d0">removeItemFromCart</data>
      <data key="d1">Method</data>
      <data key="d2">CartActionBean</data>
    </node>
    <node id="54">
      <data key="d0">updateCartQuantities</data>
      <data key="d1">Method</data>
      <data key="d2">CartActionBean</data>
    </node>
    <node id="57">
      <data key="d0">clear</data>
      <data key="d1">Method</data>
      <data key="d2">CartActionBean</data>
    </node>
    <node id="63">
      <data key="d0">getOrder</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="64">
      <data key="d0">setOrder</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="67">
      <data key="d0">isConfirmed</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="70">
      <data key="d0">getOrderList</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="71">
      <data key="d0">listOrders</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="72">
      <data key="d0">newOrderForm</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="73">
      <data key="d0">newOrder</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="74">
      <data key="d0">viewOrder</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="75">
      <data key="d0">clear</data>
      <data key="d1">Method</data>
      <data key="d2">OrderActionBean</data>
    </node>
    <node id="84">
      <data key="d0">getCategory</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="85">
      <data key="d0">setCategory</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="86">
      <data key="d0">getProduct</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="87">
      <data key="d0">setProduct</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="88">
      <data key="d0">getItem</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="89">
      <data key="d0">setItem</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="90">
      <data key="d0">getCategoryList</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="91">
      <data key="d0">setCategoryList</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="92">
      <data key="d0">getProductList</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="93">
      <data key="d0">setProductList</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="94">
      <data key="d0">getItemList</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="95">
      <data key="d0">setItemList</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="97">
      <data key="d0">viewCategory</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="98">
      <data key="d0">viewProduct</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="99">
      <data key="d0">viewItem</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="100">
      <data key="d0">searchProducts</data>
      <data key="d1">Method</data>
      <data key="d2">CatalogActionBean</data>
    </node>
    <node id="102">
      <data key="d0">getAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="103">
      <data key="d0">getUsername</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="105">
      <data key="d0">getPassword</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="107">
      <data key="d0">getMyList</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="108">
      <data key="d0">setMyList</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="112">
      <data key="d0">newAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="114">
      <data key="d0">editAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="116">
      <data key="d0">signon</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="117">
      <data key="d0">signoff</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <node id="119">
      <data key="d0">clear</data>
      <data key="d1">Method</data>
      <data key="d2">AccountActionBean</data>
    </node>
    <edge source="1" target="5">
      <data key="d3">References</data>
    </edge>
    <edge source="2" target="1">
      <data key="d3">References</data>
    </edge>
    <edge source="3" target="2">
      <data key="d3">References</data>
    </edge>
    <edge source="4" target="6">
      <data key="d3">References</data>
    </edge>
    <edge source="6" target="1">
      <data key="d3">References</data>
    </edge>
    <edge source="9" target="0">
      <data key="d3">Persists</data>
    </edge>
    <edge source="10" target="0">
      <data key="d3">Persists</data>
    </edge>
    <edge source="11" target="5">
      <data key="d3">Persists</data>
    </edge>
    <edge source="12" target="5">
      <data key="d3">Persists</data>
    </edge>
    <edge source="13" target="5">
      <data key="d3">Persists</data>
    </edge>
    <edge source="14" target="3">
      <data key="d3">Persists</data>
    </edge>
    <edge source="15" target="3">
      <data key="d3">Persists</data>
    </edge>
    <edge source="16" target="3">
      <data key="d3">Persists</data>
    </edge>
    <edge source="17" target="3">
      <data key="d3">Persists</data>
    </edge>
    <edge source="18" target="7">
      <data key="d3">Persists</data>
    </edge>
    <edge source="19" target="7">
      <data key="d3">Persists</data>
    </edge>
    <edge source="20" target="7">
      <data key="d3">Persists</data>
    </edge>
    <edge source="21" target="7">
      <data key="d3">Persists</data>
    </edge>
    <edge source="22" target="7">
      <data key="d3">Persists</data>
    </edge>
    <edge source="23" target="7">
      <data key="d3">Persists</data>
    </edge>
    <edge source="24" target="7">
      <data key="d3">Persists</data>
    </edge>
    <edge source="25" target="7">
      <data key="d3">Persists</data>
    </edge>
    <edge source="26" target="8">
      <data key="d3">Persists</data>
    </edge>
    <edge source="27" target="8">
      <data key="d3">Persists</data>
    </edge>
    <edge source="28" target="2">
      <data key="d3">Persists</data>
    </edge>
    <edge source="29" target="2">
      <data key="d3">Persists</data>
    </edge>
    <edge source="32" target="1">
      <data key="d3">Persists</data>
    </edge>
    <edge source="33" target="1">
      <data key="d3">Persists</data>
    </edge>
    <edge source="34" target="9">
      <data key="d3">Calls</data>
    </edge>
    <edge source="34" target="0">
      <data key="d3">Uses</data>
    </edge>
    <edge source="35" target="10">
      <data key="d3">Calls</data>
    </edge>
    <edge source="35" target="0">
      <data key="d3">Uses</data>
    </edge>
    <edge source="36" target="12">
      <data key="d3">Calls</data>
    </edge>
    <edge source="36" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="37" target="11">
      <data key="d3">Calls</data>
    </edge>
    <edge source="37" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="38" target="13">
      <data key="d3">Calls</data>
    </edge>
    <edge source="38" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="39" target="32">
      <data key="d3">Calls</data>
    </edge>
    <edge source="39" target="1">
      <data key="d3">Uses</data>
    </edge>
    <edge source="40" target="33">
      <data key="d3">Calls</data>
    </edge>
    <edge source="40" target="1">
      <data key="d3">Uses</data>
    </edge>
    <edge source="41" target="31">
      <data key="d3">Calls</data>
    </edge>
    <edge source="42" target="19">
      <data key="d3">Calls</data>
    </edge>
    <edge source="42" target="7">
      <data key="d3">Uses</data>
    </edge>
    <edge source="43" target="20">
      <data key="d3">Calls</data>
    </edge>
    <edge source="43" target="21">
      <data key="d3">Calls</data>
    </edge>
    <edge source="43" target="22">
      <data key="d3">Calls</data>
    </edge>
    <edge source="43" target="7">
      <data key="d3">Uses</data>
    </edge>
    <edge source="44" target="23">
      <data key="d3">Calls</data>
    </edge>
    <edge source="44" target="24">
      <data key="d3">Calls</data>
    </edge>
    <edge source="44" target="7">
      <data key="d3">Uses</data>
    </edge>
    <edge source="45" target="48">
      <data key="d3">Calls</data>
    </edge>
    <edge source="45" target="16">
      <data key="d3">Calls</data>
    </edge>
    <edge source="45" target="17">
      <data key="d3">Calls</data>
    </edge>
    <edge source="45" target="3">
      <data key="d3">Uses</data>
    </edge>
    <edge source="46" target="15">
      <data key="d3">Calls</data>
    </edge>
    <edge source="46" target="28">
      <data key="d3">Calls</data>
    </edge>
    <edge source="46" target="3">
      <data key="d3">Uses</data>
    </edge>
    <edge source="47" target="14">
      <data key="d3">Calls</data>
    </edge>
    <edge source="47" target="3">
      <data key="d3">Uses</data>
    </edge>
    <edge source="48" target="26">
      <data key="d3">Calls</data>
    </edge>
    <edge source="48" target="27">
      <data key="d3">Calls</data>
    </edge>
    <edge source="48" target="8">
      <data key="d3">Uses</data>
    </edge>
    <edge source="49" target="4">
      <data key="d3">Uses</data>
    </edge>
    <edge source="50" target="4">
      <data key="d3">Uses</data>
    </edge>
    <edge source="52" target="41">
      <data key="d3">Calls</data>
    </edge>
    <edge source="52" target="40">
      <data key="d3">Calls</data>
    </edge>
    <edge source="52" target="1">
      <data key="d3">Uses</data>
    </edge>
    <edge source="53" target="1">
      <data key="d3">Uses</data>
    </edge>
    <edge source="54" target="49">
      <data key="d3">Calls</data>
    </edge>
    <edge source="54" target="6">
      <data key="d3">Uses</data>
    </edge>
    <edge source="57" target="4">
      <data key="d3">Uses</data>
    </edge>
    <edge source="63" target="3">
      <data key="d3">Uses</data>
    </edge>
    <edge source="64" target="3">
      <data key="d3">Uses</data>
    </edge>
    <edge source="70" target="3">
      <data key="d3">Uses</data>
    </edge>
    <edge source="71" target="47">
      <data key="d3">Calls</data>
    </edge>
    <edge source="72" target="75">
      <data key="d3">Calls</data>
    </edge>
    <edge source="73" target="67">
      <data key="d3">Calls</data>
    </edge>
    <edge source="73" target="63">
      <data key="d3">Calls</data>
    </edge>
    <edge source="73" target="45">
      <data key="d3">Calls</data>
    </edge>
    <edge source="74" target="46">
      <data key="d3">Calls</data>
    </edge>
    <edge source="75" target="3">
      <data key="d3">Uses</data>
    </edge>
    <edge source="84" target="0">
      <data key="d3">Uses</data>
    </edge>
    <edge source="85" target="0">
      <data key="d3">Uses</data>
    </edge>
    <edge source="86" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="87" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="88" target="1">
      <data key="d3">Uses</data>
    </edge>
    <edge source="89" target="1">
      <data key="d3">Uses</data>
    </edge>
    <edge source="90" target="0">
      <data key="d3">Uses</data>
    </edge>
    <edge source="91" target="0">
      <data key="d3">Uses</data>
    </edge>
    <edge source="92" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="93" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="94" target="1">
      <data key="d3">Uses</data>
    </edge>
    <edge source="95" target="1">
      <data key="d3">Uses</data>
    </edge>
    <edge source="97" target="37">
      <data key="d3">Calls</data>
    </edge>
    <edge source="97" target="35">
      <data key="d3">Calls</data>
    </edge>
    <edge source="98" target="39">
      <data key="d3">Calls</data>
    </edge>
    <edge source="98" target="36">
      <data key="d3">Calls</data>
    </edge>
    <edge source="99" target="40">
      <data key="d3">Calls</data>
    </edge>
    <edge source="100" target="38">
      <data key="d3">Calls</data>
    </edge>
    <edge source="102" target="7">
      <data key="d3">Uses</data>
    </edge>
    <edge source="107" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="108" target="5">
      <data key="d3">Uses</data>
    </edge>
    <edge source="112" target="43">
      <data key="d3">Calls</data>
    </edge>
    <edge source="112" target="42">
      <data key="d3">Calls</data>
    </edge>
    <edge source="112" target="37">
      <data key="d3">Calls</data>
    </edge>
    <edge source="114" target="44">
      <data key="d3">Calls</data>
    </edge>
    <edge source="114" target="42">
      <data key="d3">Calls</data>
    </edge>
    <edge source="114" target="37">
      <data key="d3">Calls</data>
    </edge>
    <edge source="116" target="42">
      <data key="d3">Calls</data>
    </edge>
    <edge source="116" target="103">
      <data key="d3">Calls</data>
    </edge>
    <edge source="116" target="105">
      <data key="d3">Calls</data>
    </edge>
    <edge source="116" target="119">
      <data key="d3">Calls</data>
    </edge>
    <edge source="116" target="37">
      <data key="d3">Calls</data>
    </edge>
    <edge source="117" target="119">
      <data key="d3">Calls</data>
    </edge>
    <edge source="119" target="7">
      <data key="d3">Uses</data>
    </edge>
  </graph>
</graphml>
