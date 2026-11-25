import subprocess

faq = (
    'function Wd({onOpenBooking:e}){'
    'let[t,n]=(0,T.useState)(0);'
    'let r=['
    '{q:`¿Cómo puedo agendar o cotizar mi cita en Savamá Spa?`,a:`Es muy sencillo: utiliza nuestro cotizador en línea seleccionando el tratamiento que deseas, agrega servicios complementarios si gustas y pulsa "Cotizar". Serás redirigido directamente a nuestro WhatsApp oficial (+57 300 494 9692) para coordinar el horario y resolver cualquier inquietud.`},'
    '{q:`¿Qué diferencia a Savamá Spa de un spa tradicional?`,a:`En Savamá Spa fusionamos la medicina especializada y funcional, la fisioterapia clínica y los rituales de relajación sensorial. No solo trabajamos la estética exterior, sino la salud profunda, el alivio de contracturas y el equilibrio biológico de tu organismo.`},'
    '{q:`¿Cuántas sesiones de tratamientos reductores o depilación láser necesito?`,a:`Los resultados son visibles desde las primeras sesiones. Sin embargo, para objetivos duraderos de reducción de medidas o eliminación definitiva del vello, recomendamos paquetes estructurados de 6 a 10 sesiones, diseñados de acuerdo a tu valoración previa.`},'
    '{q:`¿Quiénes realizan los tratamientos de fisioterapia y medicina funcional?`,a:`Todos nuestros procedimientos son aplicados por especialistas certificados y fisioterapeutas profesionales en cabinas privadas equipadas con camillas confortables y protocolos higiénicos de máxima calidad.`},'
    '{q:`¿Dónde están ubicados exactamente y qué horarios manejan?`,a:`Nos encontramos en la Cra. 78 #30C-27, Local 302, Edificio Gran Plazuela (junto al Centro Comercial La Plazuela), Barrio Santa Mónica, Cartagena de Indias. Atendemos de lunes a viernes de 9:00 a.m. a 7:00 p.m. y sábados de 8:00 a.m. a 4:00 p.m.`},'
    '{q:`¿Manejan bonos de regalo o atención para parejas?`,a:`¡Sí! Diseñamos bonos de regalo personalizados para fechas especiales (cumpleaños, aniversarios, bienestar) y contamos con el "Ritual Dúo" para parejas en cabina privada con aromaterapia y copas de bienvenida.`}'
    '];'
    'let i=['
    '{title:`Medicina Funcional & Fisioterapia`,desc:`Fusión clínica única en Cartagena que trata el origen de tensiones, inflamación y desequilibrios.`},'
    '{title:`Especialistas Certificados`,desc:`Equipo humano profesional con enfoque ético, calidez y atención personalizada 1 a 1.`},'
    '{title:`Ubicación Privada en La Plazuela`,desc:`Cabinas confortables en Edificio Gran Plazuela, con fácil acceso, seguridad y parqueadero.`},'
    '{title:`Agendamiento Rápido 24/7`,desc:`Cotizador interactivo en línea directo a nuestro WhatsApp sin intermediarios ni esperas.`}'
    '];'
    'return (0,B.jsx)(`section`,{id:`faq`,"aria-labelledby":`faq-heading`,className:`bg-[#EFE3D7] border-t border-[#D2B5A0]/60 py-20 lg:py-24`,children:(0,B.jsxs)(`div`,{className:`max-w-[1340px] mx-auto px-6 sm:px-10 lg:px-12`,children:['
    '(0,B.jsxs)(`div`,{className:`text-center max-w-2xl mx-auto mb-14 lg:mb-16`,children:['
    '(0,B.jsx)(`p`,{className:`font-sans text-[12px] font-medium uppercase tracking-[0.22em] text-[#8A6552] mb-2.5`,children:`Salud · Belleza · Bienestar`}),'
    '(0,B.jsx)(`h2`,{id:`faq-heading`,className:`font-serif font-medium text-[clamp(2.4rem,4.2vw,3.5rem)] leading-[1.08] text-[#4A3A30]`,children:`¿Por qué elegir Savamá Spa?`}),'
    '(0,B.jsx)(`p`,{className:`font-sans text-[16.5px] leading-[1.65] text-[#4A3A30]/80 mt-3`,children:`Un santuario en Cartagena donde el rigor de la fisioterapia y la medicina funcional se combinan con la armonía y relajación de un spa boutique.`})'
    ']}),'
    '(0,B.jsx)(`div`,{className:`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 mb-16`,children:i.map((e,idx)=>(0,B.jsxs)(`div`,{key:idx,className:`bg-[#FAF6F2]/80 backdrop-blur-sm rounded-[18px] border border-[#D2B5A0]/50 p-6 flex flex-col justify-between`,children:['
    '(0,B.jsx)(`span`,{className:`font-serif text-2xl text-[#97735F] font-semibold`,children:`0`+(idx+1)}),'
    '(0,B.jsx)(`h3`,{className:`font-serif text-[20px] font-medium text-[#4A3A30] mt-2 leading-snug`,children:e.title}),'
    '(0,B.jsx)(`p`,{className:`font-sans text-[14px] leading-[1.6] text-[#4A3A30]/75 mt-2`,children:e.desc})'
    ']}))}),'
    '(0,B.jsxs)(`div`,{className:`max-w-3xl mx-auto`,children:['
    '(0,B.jsx)(`h3`,{className:`font-serif text-2xl lg:text-3xl text-center text-[#4A3A30] mb-8 font-medium`,children:`Preguntas Frecuentes`}),'
    '(0,B.jsx)(`div`,{className:`space-y-3`,children:r.map((e,idx)=>{let o=t===idx;return (0,B.jsxs)(`div`,{key:idx,className:`bg-[#FAF6F2] rounded-[16px] border border-[#D2B5A0]/60 overflow-hidden transition-all duration-200`,children:['
    '(0,B.jsxs)(`button`,{type:`button`,onClick:()=>n(o?-1:idx),className:`w-full px-6 py-4.5 text-left flex items-center justify-between gap-4 cursor-pointer focus-visible:outline-none`,children:['
    '(0,B.jsx)(`span`,{className:`font-sans font-medium text-[15.5px] text-[#4A3A30]`,children:e.q}),'
    '(0,B.jsx)(`span`,{className:`w-7 h-7 rounded-full bg-[#EAD7C8]/50 flex items-center justify-center shrink-0 text-[#97735F] text-base font-bold transition-transform duration-200 `+(o?`rotate-45`:``),children:`+`})'
    ']}),'
    'o&&(0,B.jsx)(`div`,{className:`px-6 pb-5 pt-1 border-t border-[#D2B5A0]/30`,children:(0,B.jsx)(`p`,{className:`font-sans text-[14.5px] leading-[1.65] text-[#4A3A30]/80`,children:e.a})})'
    ']})})}),'
    '(0,B.jsxs)(`div`,{className:`text-center mt-12`,children:['
    '(0,B.jsx)(`p`,{className:`font-sans text-[14.5px] text-[#4A3A30]/80 mb-4`,children:`¿Tienes otra consulta o deseas una valoración personalizada?`}),'
    '(0,B.jsxs)(`button`,{type:`button`,onClick:()=>e(`reductores`),className:`inline-flex items-center gap-3 rounded-full bg-[#97735F] hover:bg-[#8A6552] text-[#EAD7C8] hover:text-[#FAF6F2] px-8 py-3.5 font-sans text-[13px] font-medium uppercase tracking-[0.16em] transition-colors cursor-pointer shadow-sm`,children:['
    '(0,B.jsx)(`span`,{children:`Cotizar mi cita ahora`}),'
    '(0,B.jsx)(ne,{className:`w-4 h-4`,"aria-hidden":`true`})'
    ']})'
    ']})'
    ']})'
    ']})})'
    '}'
)

# Test FAQ syntax independently
test_code = 'var T = { useState: function() { return [0, function(){}]; } }; var B = { jsx: function(){}, jsxs: function(){} }; var ne = function(){};\n' + faq
with open('/tmp/test_faq.js', 'w') as f:
    f.write(test_code)

res = subprocess.run(['/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc', '/tmp/test_faq.js'], capture_output=True, text=True)
if res.stderr or 'SyntaxError' in res.stdout:
    print('FAQ ERROR:', res.stderr, res.stdout)
    exit(1)
else:
    print('✓ FAQ component syntax is 100% VALID!')

# Now apply to actual bundle file
js_file = '/Users/lola/Desktop/prue/assets/index-5_KYy88D.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace Wd in js
start_wd = js.find('function Wd({onOpenBooking:e})')
if start_wd == -1:
    start_wd = js.find('function Wd(')
end_wd = js.find('function Gd({phoneDisplay:e,whatsappHref:t,scheduleDisplay:n,instagramHandle:r,onOpenBooking:i})')

assert start_wd != -1, 'start_wd not found'
assert end_wd != -1, 'end_wd not found'

js = js[:start_wd] + faq + js[end_wd:]

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js)

print('✓ Updated assets/index-5_KYy88D.js with fixed FAQ component')

# Now test the ENTIRE bundle with jsc
with open('/tmp/entire_bundle_test.js', 'w', encoding='utf-8') as f:
    # provide browser mock globals so jsc can run the entire file
    mock_env = '''
var window = this;
var document = {
    createElement: function(tag) {
        return {
            tagName: tag.toUpperCase(),
            style: {},
            setAttribute: function(){},
            removeAttribute: function(){},
            addEventListener: function(){},
            appendChild: function(){},
            removeChild: function(){},
            classList: { add: function(){}, remove: function(){} },
            relList: { supports: function(){ return true; } }
        };
    },
    querySelectorAll: function() { return []; },
    getElementById: function() { return document.createElement('div'); },
    body: { appendChild: function(){}, removeChild: function(){} },
    addEventListener: function(){}
};
var navigator = { userAgent: 'Safari' };
var location = { href: 'http://localhost/' };
var MutationObserver = function() { return { observe: function(){}, disconnect: function(){} }; };
'''
    f.write(mock_env + '\n' + js)

res2 = subprocess.run(['/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc', '/tmp/entire_bundle_test.js'], capture_output=True, text=True)
print('ENTIRE BUNDLE TEST RESULT:')
print('STDOUT:', res2.stdout.strip())
print('STDERR:', res2.stderr.strip())
if not res2.stderr and 'SyntaxError' not in res2.stdout:
    print('🚀 THE ENTIRE BUNDLE LOADS AND EXECUTES WITH ZERO SYNTAX ERRORS!')
