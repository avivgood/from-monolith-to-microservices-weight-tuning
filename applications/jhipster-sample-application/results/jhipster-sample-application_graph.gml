<?xml version='1.0' encoding='utf-8'?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key id="d3" for="edge" attr.name="rel_type" attr.type="string" />
  <key id="d2" for="node" attr.name="class_name" attr.type="string" />
  <key id="d1" for="node" attr.name="type" attr.type="string" />
  <key id="d0" for="node" attr.name="name" attr.type="string" />
  <graph edgedefault="directed">
    <node id="2">
      <data key="d0">UserNotActivatedException</data>
      <data key="d1">Entity</data>
    </node>
    <node id="10">
      <data key="d0">PasswordChangeDTO</data>
      <data key="d1">Entity</data>
    </node>
    <node id="11">
      <data key="d0">UserDTO</data>
      <data key="d1">Entity</data>
    </node>
    <node id="12">
      <data key="d0">Authority</data>
      <data key="d1">Entity</data>
    </node>
    <node id="13">
      <data key="d0">AbstractAuditingEntity</data>
      <data key="d1">Entity</data>
    </node>
    <node id="14">
      <data key="d0">PersistentAuditEvent</data>
      <data key="d1">Entity</data>
    </node>
    <node id="15">
      <data key="d0">User</data>
      <data key="d1">Entity</data>
    </node>
    <node id="19">
      <data key="d0">EmailAlreadyUsedException</data>
      <data key="d1">Entity</data>
    </node>
    <node id="21">
      <data key="d0">InvalidPasswordException</data>
      <data key="d1">Entity</data>
    </node>
    <node id="22">
      <data key="d0">BadRequestAlertException</data>
      <data key="d1">Entity</data>
    </node>
    <node id="23">
      <data key="d0">LoginAlreadyUsedException</data>
      <data key="d1">Entity</data>
    </node>
    <node id="25">
      <data key="d0">LoginVM</data>
      <data key="d1">Entity</data>
    </node>
    <node id="26">
      <data key="d0">ManagedUserVM</data>
      <data key="d1">Entity</data>
    </node>
    <node id="27">
      <data key="d0">KeyAndPasswordVM</data>
      <data key="d1">Entity</data>
    </node>
    <node id="29">
      <data key="d0">createSpringSecurityUser</data>
      <data key="d1">Method</data>
      <data key="d2">DomainUserDetailsService</data>
    </node>
    <node id="32">
      <data key="d0">createToken</data>
      <data key="d1">Method</data>
      <data key="d2">TokenProvider</data>
    </node>
    <node id="33">
      <data key="d0">getAuthentication</data>
      <data key="d1">Method</data>
      <data key="d2">TokenProvider</data>
    </node>
    <node id="35">
      <data key="d0">sendEmail</data>
      <data key="d1">Method</data>
      <data key="d2">MailService</data>
    </node>
    <node id="36">
      <data key="d0">sendEmailFromTemplate</data>
      <data key="d1">Method</data>
      <data key="d2">MailService</data>
    </node>
    <node id="37">
      <data key="d0">sendActivationEmail</data>
      <data key="d1">Method</data>
      <data key="d2">MailService</data>
    </node>
    <node id="38">
      <data key="d0">sendCreationEmail</data>
      <data key="d1">Method</data>
      <data key="d2">MailService</data>
    </node>
    <node id="39">
      <data key="d0">sendPasswordResetMail</data>
      <data key="d1">Method</data>
      <data key="d2">MailService</data>
    </node>
    <node id="40">
      <data key="d0">activateRegistration</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="41">
      <data key="d0">completePasswordReset</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="42">
      <data key="d0">requestPasswordReset</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="43">
      <data key="d0">registerUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="44">
      <data key="d0">removeNonActivatedUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="45">
      <data key="d0">createUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="46">
      <data key="d0">updateUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="47">
      <data key="d0">deleteUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="48">
      <data key="d0">changePassword</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="49">
      <data key="d0">getAllManagedUsers</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="50">
      <data key="d0">getUserWithAuthoritiesByLogin</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="51">
      <data key="d0">getUserWithAuthorities</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="53">
      <data key="d0">getAuthorities</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="54">
      <data key="d0">clearUserCaches</data>
      <data key="d1">Method</data>
      <data key="d2">UserService</data>
    </node>
    <node id="56">
      <data key="d0">findAll</data>
      <data key="d1">Method</data>
      <data key="d2">AuditEventService</data>
    </node>
    <node id="57">
      <data key="d0">findByDates</data>
      <data key="d1">Method</data>
      <data key="d2">AuditEventService</data>
    </node>
    <node id="58">
      <data key="d0">find</data>
      <data key="d1">Method</data>
      <data key="d2">AuditEventService</data>
    </node>
    <node id="59">
      <data key="d0">usersToUserDTOs</data>
      <data key="d1">Method</data>
      <data key="d2">UserMapper</data>
    </node>
    <node id="60">
      <data key="d0">userToUserDTO</data>
      <data key="d1">Method</data>
      <data key="d2">UserMapper</data>
    </node>
    <node id="61">
      <data key="d0">userDTOsToUsers</data>
      <data key="d1">Method</data>
      <data key="d2">UserMapper</data>
    </node>
    <node id="62">
      <data key="d0">userDTOToUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserMapper</data>
    </node>
    <node id="63">
      <data key="d0">authoritiesFromStrings</data>
      <data key="d1">Method</data>
      <data key="d2">UserMapper</data>
    </node>
    <node id="64">
      <data key="d0">userFromId</data>
      <data key="d1">Method</data>
      <data key="d2">UserMapper</data>
    </node>
    <node id="65">
      <data key="d0">convertToAuditEvent</data>
      <data key="d1">Method</data>
      <data key="d2">AuditEventConverter</data>
    </node>
    <node id="66">
      <data key="d0">convertDataToObjects</data>
      <data key="d1">Method</data>
      <data key="d2">AuditEventConverter</data>
    </node>
    <node id="67">
      <data key="d0">convertDataToStrings</data>
      <data key="d1">Method</data>
      <data key="d2">AuditEventConverter</data>
    </node>
    <node id="69">
      <data key="d0">getAll</data>
      <data key="d1">Method</data>
      <data key="d2">AuditResource</data>
    </node>
    <node id="70">
      <data key="d0">getByDates</data>
      <data key="d1">Method</data>
      <data key="d2">AuditResource</data>
    </node>
    <node id="71">
      <data key="d0">get</data>
      <data key="d1">Method</data>
      <data key="d2">AuditResource</data>
    </node>
    <node id="72">
      <data key="d0">createUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserResource</data>
    </node>
    <node id="73">
      <data key="d0">updateUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserResource</data>
    </node>
    <node id="74">
      <data key="d0">getAllUsers</data>
      <data key="d1">Method</data>
      <data key="d2">UserResource</data>
    </node>
    <node id="75">
      <data key="d0">onlyContainsAllowedProperties</data>
      <data key="d1">Method</data>
      <data key="d2">UserResource</data>
    </node>
    <node id="76">
      <data key="d0">getAuthorities</data>
      <data key="d1">Method</data>
      <data key="d2">UserResource</data>
    </node>
    <node id="77">
      <data key="d0">getUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserResource</data>
    </node>
    <node id="78">
      <data key="d0">deleteUser</data>
      <data key="d1">Method</data>
      <data key="d2">UserResource</data>
    </node>
    <node id="79">
      <data key="d0">registerAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountResource</data>
    </node>
    <node id="80">
      <data key="d0">activateAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountResource</data>
    </node>
    <node id="82">
      <data key="d0">getAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountResource</data>
    </node>
    <node id="83">
      <data key="d0">saveAccount</data>
      <data key="d1">Method</data>
      <data key="d2">AccountResource</data>
    </node>
    <node id="84">
      <data key="d0">changePassword</data>
      <data key="d1">Method</data>
      <data key="d2">AccountResource</data>
    </node>
    <node id="85">
      <data key="d0">requestPasswordReset</data>
      <data key="d1">Method</data>
      <data key="d2">AccountResource</data>
    </node>
    <node id="86">
      <data key="d0">finishPasswordReset</data>
      <data key="d1">Method</data>
      <data key="d2">AccountResource</data>
    </node>
    <node id="87">
      <data key="d0">checkPasswordLength</data>
      <data key="d1">Method</data>
      <data key="d2">AccountResource</data>
    </node>
    <node id="88">
      <data key="d0">authorize</data>
      <data key="d1">Method</data>
      <data key="d2">UserJWTController</data>
    </node>
    <node id="89">
      <data key="d0">find</data>
      <data key="d1">Method</data>
      <data key="d2">CustomAuditEventRepository</data>
    </node>
    <node id="90">
      <data key="d0">add</data>
      <data key="d1">Method</data>
      <data key="d2">CustomAuditEventRepository</data>
    </node>
    <node id="91">
      <data key="d0">truncate</data>
      <data key="d1">Method</data>
      <data key="d2">CustomAuditEventRepository</data>
    </node>
    <edge source="15" target="12">
      <data key="d3">References</data>
    </edge>
    <edge source="15" target="13">
      <data key="d3">Extends</data>
    </edge>
    <edge source="19" target="22">
      <data key="d3">Extends</data>
    </edge>
    <edge source="23" target="22">
      <data key="d3">Extends</data>
    </edge>
    <edge source="26" target="11">
      <data key="d3">Extends</data>
    </edge>
    <edge source="29" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="29" target="2">
      <data key="d3">Uses</data>
    </edge>
    <edge source="33" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="36" target="35">
      <data key="d3">Calls</data>
    </edge>
    <edge source="36" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="37" target="36">
      <data key="d3">Calls</data>
    </edge>
    <edge source="37" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="38" target="36">
      <data key="d3">Calls</data>
    </edge>
    <edge source="38" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="39" target="36">
      <data key="d3">Calls</data>
    </edge>
    <edge source="39" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="40" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="41" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="42" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="43" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="43" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="43" target="12">
      <data key="d3">Uses</data>
    </edge>
    <edge source="44" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="45" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="45" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="45" target="12">
      <data key="d3">Uses</data>
    </edge>
    <edge source="49" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="50" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="51" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="54" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="59" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="59" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="60" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="60" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="61" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="61" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="62" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="62" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="62" target="12">
      <data key="d3">Uses</data>
    </edge>
    <edge source="63" target="12">
      <data key="d3">Uses</data>
    </edge>
    <edge source="64" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="65" target="66">
      <data key="d3">Calls</data>
    </edge>
    <edge source="65" target="14">
      <data key="d3">Uses</data>
    </edge>
    <edge source="69" target="56">
      <data key="d3">Calls</data>
    </edge>
    <edge source="70" target="57">
      <data key="d3">Calls</data>
    </edge>
    <edge source="71" target="58">
      <data key="d3">Calls</data>
    </edge>
    <edge source="72" target="45">
      <data key="d3">Calls</data>
    </edge>
    <edge source="72" target="38">
      <data key="d3">Calls</data>
    </edge>
    <edge source="72" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="72" target="22">
      <data key="d3">Uses</data>
    </edge>
    <edge source="72" target="23">
      <data key="d3">Uses</data>
    </edge>
    <edge source="72" target="19">
      <data key="d3">Uses</data>
    </edge>
    <edge source="72" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="73" target="46">
      <data key="d3">Calls</data>
    </edge>
    <edge source="73" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="73" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="73" target="19">
      <data key="d3">Uses</data>
    </edge>
    <edge source="73" target="23">
      <data key="d3">Uses</data>
    </edge>
    <edge source="74" target="75">
      <data key="d3">Calls</data>
    </edge>
    <edge source="74" target="49">
      <data key="d3">Calls</data>
    </edge>
    <edge source="74" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="76" target="53">
      <data key="d3">Calls</data>
    </edge>
    <edge source="77" target="50">
      <data key="d3">Calls</data>
    </edge>
    <edge source="77" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="78" target="47">
      <data key="d3">Calls</data>
    </edge>
    <edge source="79" target="87">
      <data key="d3">Calls</data>
    </edge>
    <edge source="79" target="43">
      <data key="d3">Calls</data>
    </edge>
    <edge source="79" target="37">
      <data key="d3">Calls</data>
    </edge>
    <edge source="79" target="26">
      <data key="d3">Uses</data>
    </edge>
    <edge source="79" target="21">
      <data key="d3">Uses</data>
    </edge>
    <edge source="79" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="80" target="40">
      <data key="d3">Calls</data>
    </edge>
    <edge source="80" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="82" target="51">
      <data key="d3">Calls</data>
    </edge>
    <edge source="82" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="83" target="46">
      <data key="d3">Calls</data>
    </edge>
    <edge source="83" target="11">
      <data key="d3">Uses</data>
    </edge>
    <edge source="83" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="83" target="19">
      <data key="d3">Uses</data>
    </edge>
    <edge source="84" target="87">
      <data key="d3">Calls</data>
    </edge>
    <edge source="84" target="48">
      <data key="d3">Calls</data>
    </edge>
    <edge source="84" target="10">
      <data key="d3">Uses</data>
    </edge>
    <edge source="84" target="21">
      <data key="d3">Uses</data>
    </edge>
    <edge source="85" target="42">
      <data key="d3">Calls</data>
    </edge>
    <edge source="85" target="39">
      <data key="d3">Calls</data>
    </edge>
    <edge source="85" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="86" target="87">
      <data key="d3">Calls</data>
    </edge>
    <edge source="86" target="41">
      <data key="d3">Calls</data>
    </edge>
    <edge source="86" target="27">
      <data key="d3">Uses</data>
    </edge>
    <edge source="86" target="21">
      <data key="d3">Uses</data>
    </edge>
    <edge source="86" target="15">
      <data key="d3">Uses</data>
    </edge>
    <edge source="88" target="32">
      <data key="d3">Calls</data>
    </edge>
    <edge source="88" target="25">
      <data key="d3">Uses</data>
    </edge>
    <edge source="89" target="65">
      <data key="d3">Calls</data>
    </edge>
    <edge source="89" target="14">
      <data key="d3">Persists</data>
    </edge>
    <edge source="90" target="67">
      <data key="d3">Calls</data>
    </edge>
    <edge source="90" target="91">
      <data key="d3">Calls</data>
    </edge>
    <edge source="90" target="14">
      <data key="d3">Persists</data>
    </edge>
  </graph>
</graphml>
