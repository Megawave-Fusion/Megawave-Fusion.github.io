import test from 'node:test';
import assert from 'node:assert/strict';
import {searchEntries} from '../site/assets/search-core.mjs';
const entries = [
 {title:'原理与适用条件',text:'少数离子加热与共振',tag:'MF000010',chapter_slug:'heating',chapter_title:'辅助加热',section_title:'离子回旋加热（ICRH / ICRF）',kind:'条目',order:1},
 {title:'原理与适用条件',text:'中性束慢化与轨道',tag:'MF000020',chapter_slug:'heating',section_title:'中性束注入（NBI / NBCD）',kind:'条目',order:2},
 {title:'约束与性能指标',text:'ICRH 加热的能量收支',tag:'MF000003',chapter_slug:'foundations',kind:'条目',order:3},
 {title:'ITER 参考入口',text:'公开机构来源',chapter_slug:'literature',kind:'文献',order:4}
];
test('Chinese body search finds the matching mechanism',()=>assert.deepEqual(searchEntries(entries,'少数离子').map(e=>e.tag),['MF000010']));
test('English acronym uses section context and outranks incidental body mentions',()=>assert.deepEqual(searchEntries(entries,'icrh').map(e=>e.tag),['MF000010','MF000003']));
test('Exact permanent tag is case-insensitive and supports full-width input',()=>assert.equal(searchEntries(entries,'ｍｆ００００２０')[0].tag,'MF000020'));
test('Keywords use AND semantics across heading and body',()=>assert.equal(searchEntries(entries,'ICRH 共振').length,1));
test('Chapter and kind filters are combined',()=>assert.deepEqual(searchEntries(entries,'','literature','文献').map(e=>e.title),['ITER 参考入口']));
test('Unknown terms yield no unrelated results',()=>assert.equal(searchEntries(entries,'not-a-real-phrase').length,0));
